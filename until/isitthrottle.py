# -*- coding: utf-8 -*-
import time
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle

from .redis import Redis


class VisitThrottle(BaseThrottle):

    def __init__(self):
        self.redis = Redis()

    def allow_request(self, request, view):
        # 获取用户ip
        remote_addr = self.get_ident(request)
        # 第一次访问
        history = 1
        timeout = 10
        sss = self.redis.setnx(remote_addr, timeout)
        if sss:
            history = int(self.redis.get(remote_addr))
            if history > 3:
                return False
            history += 1
        self.redis.set(remote_addr, history)  # 存储额外信息
        return True




class VisitThrottle_with_not_one(SimpleRateThrottle):
    """
    匿名用户访问控制
    """
    scope = 'not_one'

    def get_cache_key(self, request, view):
        # 获取ip 也可以其他
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
    """
    登录用户访问控制
    """
    scope = 'user_has'

    def get_cache_key(self, request, view):
        pass
