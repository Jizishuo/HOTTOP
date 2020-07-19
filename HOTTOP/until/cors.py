# -*- coding: utf-8 -*-

class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CORSmiddleware(MiddlewareMixin):
    """
    自定义中间件 -- 解决跨域
    """

    def process_response(self, request, response):
        """
        response['Access-Control-Allow-Origin'] = '*' 允许所有
        或'http://127.0.0.1:8000/，....'
        :param request:
        :param response:
        :return:
        """
        response['Access-Control-Allow-Origin'] = '*'

        # 允许携带Content-Type请求头
        # response['Access-Control-Allow-Headers'] = 'Content-Type,'

        # 允许发送delete,put请求
        # response['Access-Control-Allow-Methods'] = 'DELETE, PUT,'

        return response
