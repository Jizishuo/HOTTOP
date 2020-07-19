# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = '必须是svip才能访问'

    def has_permission(self, request, view):
        # if request.user.user_type != 3:
        #     return False
        return True

