"""
You can build a custom authentication backend by subclassing the
BaseAuthentication class provided by REST framework and overriding
the authenticate() method.
"""
"""
custom permission class. Django provides a BasePermission class that allows
you to define the following methods:
has_permission(): View-level permission check
has_object_permission(): Instance-level permission check
These methods should return True to grant access or False otherwise.
"""
from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()