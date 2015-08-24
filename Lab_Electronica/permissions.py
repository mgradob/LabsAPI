__author__ = 'ardzoht'

from rest_framework import permissions
from LabsIndex.models import Administrator, Student


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return isinstance(request.user, Administrator)


class IsRegisteredStudentOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        return isinstance(request.user, Student)
