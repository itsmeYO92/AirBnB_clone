#!/usr/bin/python3
""" This module defines city class """


from models.base_model import BaseModel


class City(BaseModel):
    """ state class defined by name of the state """
    name = ""
    state_id = ""
