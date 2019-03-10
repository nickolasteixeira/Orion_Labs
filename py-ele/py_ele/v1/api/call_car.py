# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas
from . import elevator

class CallCar(Resource):

    def get(self, floor_id):

        letter = elevator.floor_map.get(floor_id)
        if not letter:
            return {'message': 'Incorrect floor id'}, 400, None      

        return {'message': elevator.call_car(floor_id)}, 200, None
