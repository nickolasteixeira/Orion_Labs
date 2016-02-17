# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas


class Welcome(Resource):

    def get(self):

        return {'msg': 'something'}, 200, None