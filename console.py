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
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review}

    def precmd(self, line):
        """
        checks if the command is a method call and parse\
        the command to the standard syntax
        """
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
        """ Quit the console """
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """ handles the EOF charachter """
        print()
        return True

    def do_create(self, line):
        """
            Creates an instance
            Usage: create <class name>
            E.g. create User
            STDOUT: ID of the created instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            my_model = self.classes[line]()
            print("{}".format(my_model.id))
            my_model.save()

    def do_show(self, line):
        """
            Shows an instance by ID
            Usage: show <class name> <ID>
            E.g. show City 1234-1234-1234
            STDOUT: String representation of an instance
        """
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
        my_object = objects.get(args[0] + "." + args[1])
        if my_object is not None:
            print(my_object)
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        """
            Destroys an instance by ID
            Usage: destroy <class name> <ID>
            E.g. destroy User 1234-1234-1234
        """
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
        """
            Shows all instances
            Usage: all <class name>
                    class name is optional
                    if no class name is provided it returns
                    all instances regardless of the classe
            E.g. all
                 all User
            STDOUT: all instances
        """
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
        """
        Updates an instance based on the class name\
        and id by adding or updating attribute
        """
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

    def do_count(self, line):
        """ count the instances of a class """
        if line == "" or line is None:
            print("** class name missing **")
            return

        count = 0
        if line in self.classes.keys():
            for k in storage.all():
                if line == k.split(".")[0]:
                    count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
