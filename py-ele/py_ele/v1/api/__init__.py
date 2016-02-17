# -*- coding: utf-8 -*-
import flask_restful as restful

from ..validators import request_validate, response_filter


class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]


class Vator(object):

    def __init__(self):
        self.floor_list = ['B2', 'B1', 'MZ', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7']

    def floor_count(self):
        return len(self.floor_list)

elevator = Vator()
