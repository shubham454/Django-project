from rest_framework import serializers
from .models import Member, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(read_only=True,
                                                many=True)

    class Meta:
        model = Member
        fields = ['member', 'real_name', 'tz', 'activity_periods']