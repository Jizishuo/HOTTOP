# -*- coding: utf-8 -*-
import json
import pickle

import redis
from django.conf import settings
from redis import Redis as PyRedis
from . func import *

@singleton
class Redis(PyRedis):
    def __init__(self, *args):
        args = settings.REDIS_CONFIG
        super().__init__(**args)

    def get(self, name, default=None):
        res = super().get(name)
        return res if res else default

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        return super().set(name, available_value(value), ex=ex, px=px, nx=nx, xx=xx)

    def set_dict(self, name, value):
        return self.set_pickle(name, value)

    def get_dict(self, name, default={}):
        return self.get_pickle(name, default)


    def set_pickle(self, name, value):
        return self.set(name, pickle.dumps(value, 0).decode())

    def get_pickle(self, name, default=None):
        res = self.get(name)
        return pickle.loads(res.encode()) if res else default


