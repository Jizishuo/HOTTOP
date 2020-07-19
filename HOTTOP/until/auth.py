# -*- coding: utf-8 -*-
from index.models import Profile
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication



class MyAuthentication(BaseAuthentication):
    # 请求前做判断（可以设置登录权限）
    def authenticate(self, request):
        token = request._request.GET.get("token")
        """
        token_obj = Usertoken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')

        return (token_obj.user, token_obj)
        """
    def authenticate_header(self, val):
        pass
