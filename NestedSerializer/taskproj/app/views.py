from .models import Member
from .serializers import MemberSerializer
from rest_framework.generics import ListAPIView


class MemberListView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
