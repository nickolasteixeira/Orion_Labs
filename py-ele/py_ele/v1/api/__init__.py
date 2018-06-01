# -*- coding: utf-8 -*-
import hashlib

import flask_restful as restful

from ..validators import request_validate, response_filter


class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]


class Vator(object):

    def __init__(self, floors, car_ct=1):
        self.floor_list = floors

        first_floor = None
        self.floor_map = {}
        for ix in range(len(floors)):
            unhashed_floor = ('floor-%s' % ix).encode('utf-8')
            fid = hashlib.sha1(unhashed_floor).hexdigest()
            self.floor_map[fid] = floors[ix]
            if first_floor is None:
                first_floor = fid

        self.car_map = {}
        self.car_current_floor = {}
        for ix in range(car_ct):
            name = ('Car-%s' % ix).encode('utf-8')
            cid = hashlib.sha1(name).hexdigest()
            self.car_map[cid] = name
            self.car_current_floor[cid] = first_floor

    def floor_count(self):
        return len(self.floor_list)

    def inventory(self):
        results = []
        for fid, name in self.floor_map.iteritems():
            results.append({'id': fid, 'name': name})
        for fid, name in self.car_map.iteritems():
            results.append({'id': fid, 'name': name})
        return results

    def current_floor(self, car_id):
        floor_id = self.car_current_floor[car_id]
        return {'id': floor_id, 'name': self.floor_map[floor_id]}


elevator = Vator(['B2', 'B1', 'MZ', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'], 2)
