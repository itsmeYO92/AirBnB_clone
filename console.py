#!/usr/bin/python3
""" airbnb console module """


import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command line console """
    
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User,
                "State": State,
                "City": City,
                "Amenity.py": Amenity,
                "Place": Place,
                "Review": Review}

    def precmd(self, line):
        """ checks if the command is a method call and parse the command to the standard syntax """
        pattern = r"^(\w+)\.(\w+)\((.*)\)"
        match = re.search(pattern, line)
        if match:
            __class = match.group(1)
            command = match.group(2)
            arg = match.group(3)
            new_args = ""
            if arg:
                args = arg.split(", ")
                for i in args:
                    new_args += i.strip('"').strip() + " "
                    
            new_line = "{} {} {}".format(command, __class, new_args)
            return new_line
        else:
            return line


    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        print()
        return True

    def do_create(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            my_model = self.classes[line]()
            print("{}".format(my_model.id))
            my_model.save()

    def do_show(self, line):
        if line == "" or line is None:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        
        
        objects = storage.all()
        my_object = objects.get( args[0] + "." + args[1])
        if my_object is not None:
            print(my_object)
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        if line == "" or line is None:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        
        
        objects = storage.all()
        key = args[0] + "." + args[1]
        my_object = objects.get(key)
        if my_object is not None:
            del storage.all()[key]
            del my_object
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        if line == "" or line is None:
            line = "all"
        args = line.split()
        if args[0] not in self.classes.keys() and args[0] != "all":
                print("** class doesn't exist **")
                return
        
        my_list = []
        for k, v in storage.all().items():
            if k.split(".")[0] == args[0] or line == "all":
                my_list.append(str(v))

        print(my_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        if line == "" or line is None:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            objects = storage.all()
            setattr(objects[key], args[2].strip('"'), args[3].strip('"'))
            storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
