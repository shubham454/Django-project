from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import (Paginator, EmptyPage,
                                   PageNotAnInteger)
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.generic import ListView
from taggit.models import Tag
from django.db.models import Count


def post_list(request, tag_slug=None):
    """This function contain pagination and list of that total data
     for that page this function is not used for generic view"""
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)  # 3 posts in each page aat a time
    page = request.GET.get('page')  # it will get page number that we want
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if post is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # it page is out of range, deliver last page of result
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    """
    for details of particular record in list
    """
    try:
        post = get_object_or_404(Post, slug=post,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    except Post.DoesNotExist:
        return HttpResponse('<h1>object not exist</h1>')
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            # Save the current post to the comment
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    # print(post_tags_ids)
    similar_posts = Post.published.filter(tags__in=post_tags_ids). \
        exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')). \
                        order_by('-same_tags', '-publish')[:4]
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts})


# class based view
class PostListView(ListView):
    """
    class based view which list out all the record with pagination but the same html page can not be render for this
    class we require some modification but only for pagination page rendering not for list
    """
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    """
    this will send email to particular person after filling the complete
    form by that person for that e are using an EmailForm to get data
    """
    # Retrive post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # all data after validation
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = '{} ({}) recommends you reading "' \
                      '{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:' \
                      '{}"'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd.get('to', None)], fail_silently=False)
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
