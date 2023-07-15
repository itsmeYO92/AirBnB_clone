#!/usr/bin/python3
""" This module defines the review class """


from models.base_model import BaseModel


class Review(BaseModel):
    """ review class """
    text = ""
    place_id = ""
    user_id = ""
