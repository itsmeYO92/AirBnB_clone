#!/usr/bin/python3
"""
    BaseModel - a module that defines all common
                attributes/methods for other classes
"""


import uuid
from datetime import datetime as time
from models import storage


class BaseModel:
    """ class to define all common attributes/methods """

    def __init__(self, *args, **kwargs):
        """ initialize an instance """
        if kwargs:
            for k, v in kwargs.items():
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, time.strptime(v, time_format))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = time.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        return the string representation of an instance
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ modifies the date of update for the instance """
        self.updated_at = time.now()
        storage.save()

    def to_dict(self):
        """ eturns a dictionary containing all keys/values\
        of __dict__ of the instance: """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
