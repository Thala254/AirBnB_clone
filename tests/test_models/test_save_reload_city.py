#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.city import City

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new City --")
my_city = City()
my_city.name = "Nakuru"
my_city.save()
print(my_city)

print("-- Create a new City 2 --")
my_city2 = City()
my_city2.name = "Eldoret"
my_city2.save()
print(my_city2)
