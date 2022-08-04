#!/usr/bin/python3
from models import base_model, user, state, city, amenity, place, review 
from models.engine import file_storage

BaseModel = base_model.BaseModel
User = user.User
State = state.State
City = city.City
Amenity = amenity.Amenity
Place = place.Place
Review = review.Review
classes = {"BaseModel": BaseModel, "User": User, "State" : State,
           "City" : City, "Amenity" : Amenity, "Place" : Place,
           "Review" : Review}
storage = file_storage.FileStorage()
storage.reload()
