#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new place --")
my_place = Place()
my_place.name = "Skycrow"
my_place.description = "chill place"
my_place.number_rooms = 35
my_place.number_bathrooms = 2
my_place.max_guest = 30
my_place.price_by_night = 4500
my_place.latitude = 57.4
my_place.longitude = 35.2
my_place.save()
print(my_place)

print("-- Create a new place 2 --")
my_place2 = Place()
my_place2.name = "Borderland"
my_place2.description = "great ambience"
my_place2.number_rooms = 25
my_place2.number_bathrooms = 15
my_place2.max_guest = 300
my_place2.price_by_night = 1500
my_place2.latitude = 60.7
my_place2.longitude = 40.4
my_place2.save()
print(my_place2)
