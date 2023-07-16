#!/usr/bin/python3
""" storage engine module """


import json


class FileStorage:
    """ File storage class to store python objects in a file in JSON """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary object """

        return self.__objects

    def new(self, obj):
        """ adds an object to the objects dicionary """

        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serialise an object and save it to a file """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()

        with open(self.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(json_dict, f)
        f.close()

    def reload(self):
        """ reload objects from a file """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User,
                   "State": State,
                   "City": City,
                   "Amenity.py": Amenity,
                   "Place": Place,
                   "Review": Review}
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                loaded_json = json.load(f)
                for k, v in loaded_json.items():
                    loaded_json[k] = classes[v["__class__"]](**v)
                self.__objects = dict(loaded_json)
            f.close()
        except FileNotFoundError:
            pass
