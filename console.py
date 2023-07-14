#!/usr/bin/python3
""" airbnb console module """


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ command line console """
    
    prompt = "(hbnb)"
    classes = ["BaseModel"]
    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_create(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            print("{}".format(my_model.id))
            my_model.save()

    def do_show(self, line):
        if line == "" or line is None:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.classes:
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
        if args[0] not in self.classes:
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
        if args[0] not in self.classes and args[0] != "all":
                print("** class doesn't exist **")
                return
        
        my_list = []
        for k, v in storage.all().items():
            if k.split(".")[0] == args[0] or line == "all":
                my_list.append(str(v))

        print(my_list)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
