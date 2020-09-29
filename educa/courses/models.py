from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    students = models.ManyToManyField(User,
                                      related_name='courses_joined',
                                      blank=True)
    owner = models.ForeignKey(User,
                              related_name='modules',
                              on_delete=models.CASCADE)
    """one subject should have one or many course that why
     we should use one to many fields"""
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    """
    a limit_choices_to argument to limit the ContentType objects that
    can be used for the generic relationship. We use the model__in field
    lookup to filter the query to the ContentType objects with a model
    attribute that is 'text', 'video', 'image', or 'file'.
    """
    module = models.ForeignKey(Module,
                               # related_name='contents',
                               on_delete=models.CASCADE,
                               limit_choices_to={'model__in': (
                                   'text',
                                   'video',
                                   'image',
                                   'file',
                               )})
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    """
    Django allows us
    to specify a placeholder for the model class name in the related_name
    attribute as %(class)s. By doing so, related_name for each child model will
    be generated automatically. Since we use '%(class)s_related' as
    related_name, the reverse relation for child models will
    be text_related, file_related, image_related, and video_related respectively.
    """
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        """This method uses the render_to_string() function for rendering a
        template and returning the rendered content as a string. Each kind
        of content is rendered using a template named after the content
        model. We use self._meta.model_name to generate the appropriate
        template name for each content model dynamically. The render()
        method provides a common interface for rendering diverse content"""
        return render_to_string('courses/content/{}.html'.format(
            self._meta.model_name), {'item': self})


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
