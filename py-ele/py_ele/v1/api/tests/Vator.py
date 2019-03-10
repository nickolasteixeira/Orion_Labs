# -*- coding: utf-8 -*-
import hashlib
from pprint import pprint


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
        '''
            find_cloest_car - returns the car id (cid) of the closest car
            floor_id - (str) - floor_id that matches with the floor letter.
            return - the car id (cid) of the closest
        '''

        # if a car is on that floor, it returns the cid of the car
        for key, val in self.car_current_floor.items():
            if floor_id == val:
                return key

        # if not on that floor, it finds the closest car
        # Build a list of indexes of where all the cars at (based on the order of the floor_list that was passed
        # when initializing the object instance) 
        letter = self.floor_map.get(floor_id)
        current_car_floor_list = []
        for fid, alpha in self.car_current_floor.items():
            current_car_floor_list.append(self.floor_list.index(self.floor_map[alpha]))

        closest = len(self.floor_map)
        letter_idx = self.floor_list.index(letter)
        
        # loop through the list and find the closest distance between floor_id and the current_car_list
        for idx in current_car_floor_list:    
            diff = abs(letter_idx - idx)
            if diff < closest:
                closest = diff
                closest_letter = self.floor_list[idx]
          
        # finds the floor id associated with the closest letter 
        for key, value in self.floor_map.items():
            if value == closest_letter:
                floor_map_key = key

        # finds the car id associated with the floor id with the closest letter
        for key, value in self.car_current_floor.items():
            if value == floor_map_key:
                return key 
                

    def call_car(self, floor_id):
        '''
            call_car - finds the closest car and updates the car_current_floor list
            
            floor_id - (str) - floor_id that matches with the floor letter. Finds the closest car to that floor_id and updates
            the self.car_current_floor map
            return - Message to the client if a successful moves occurs
        '''
        closest_car = self.find_closest_car(floor_id)
        self.car_current_floor[closest_car] = floor_id
        return "{} has been moved to Floor {}".format(self.car_map[closest_car].decode("utf-8"), self.floor_map[floor_id])


#elevator = Vator(['B2', 'B1', 'MZ', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'], 2)
