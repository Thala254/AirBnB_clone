#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Review --")
my_review = Review()
my_review.text = "Awesome state"
my_review.save()
print(my_review)

print("-- Create a new Review 2 --")
my_review2 = Review()
my_review2.text = "Great state to visit"
my_review2.save()
print(my_review2)
