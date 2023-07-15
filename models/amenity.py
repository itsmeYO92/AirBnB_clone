#!/usr/bin/python3
""" This module defines Amenity class """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ state class defined by name of the amenity """
    name = ""
