# -*- coding: utf-8 -*-
import hashlib
from pprint import pprint

import flask_restful as restful

from ..validators import request_validate, response_filter


class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]


class Vator(object):

    def __init__(self, floors, car_ct=1):
        self.floor_list = floors

        self.first_floor = None
        self.floor_map = {}
        for ix in range(len(floors)):
            unhashed_floor = ('floor-%s' % ix).encode('utf-8')
            fid = hashlib.sha1(unhashed_floor).hexdigest()
            self.floor_map[fid] = floors[ix]
            if self.first_floor is None:
                self.first_floor = fid

        self.car_map = {}
        self.car_current_floor = {}
        for ix in range(car_ct):
            name = ('Car-%s' % ix).encode('utf-8')
            cid = hashlib.sha1(name).hexdigest()
            self.car_map[cid] = name
            self.car_current_floor[cid] = self.first_floor

        print("FLOOR LIST") 
        pprint(self.floor_list)
        print("FIRST FLOOR")
        pprint(self.first_floor)
        print("FLOOR MAP") 
        pprint(self.floor_map)
        print("CAR MAP")
        pprint(self.car_map)
        print("CAR CURRENT_FLOOR")
        pprint(self.car_current_floor)

    def floor_count(self):
        return len(self.floor_list)

    def inventory(self):
        results = []
        for fid, name in self.floor_map.items():
            results.append({'id': fid, 'name': name})
        for fid, name in self.car_map.items():
            results.append({'id': fid, 'name': name.decode("utf-8")})
        return results

    def current_floor(self, car_id):
        floor_id = self.car_current_floor[car_id]
        return {'id': floor_id, 'name': self.floor_map[floor_id]}

    def find_closest_car(self, floor_id):
        # To be completed
        pass

    def call_car(self, floor_id):
        # To be completed
        pass


elevator = Vator(['B2', 'B1', 'MZ', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'], 2)
