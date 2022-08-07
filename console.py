#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
import json
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User,
               "Amenity": Amenity, "City": City, "Place": Place,
               "Review": Review, "State": State}

    def do_EOF(self, line):
        """
            Exit on Ctrl + D
        """
        print()
        return True

    def do_quit(self, line):
        """
            Exit on quit : quit
        """
        return True

    def emptyline(self):
        """
            Overwrite default behavior to repeat last command
        """
        pass

    def do_create(self, line):
        """
            Create instance specified by user
            Usage: create <Class name> <attr1=val1> <attr2=val2>...

            **Arguments**
                Class name: required
                key=value pairs
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                instance = HBNBCommand.classes[args[0]]()
            else:
                result = self.__parse_args(args[1:])
                if result is None:
                    print("** Object fails **")
                    return
                instance = HBNBCommand.classes[args[0]](**result)
                instance.save()
                print(instance.id)

    def __parse_args(self, a_list):
        """
           Parses the list of key value args to a dictionary

           **Return**
                a dictionary or None
        """
        try:
            result = dict([x.split("=") for x in a_list])
        except ValueError:
            print("Wrong format in the attribute=value pairs")
            return None
        for key in result.keys():
            if "." in result[key]:
                try:
                    result[key] = float(result[key])
                    continue
                except (TypeError, ValueError):
                    pass
            else:
                try:
                    result[key] = int(result[key])
                    continue
                except (TypeError, ValueError):
                    pass
            if (result[key].count('"') == (result[key].count('\\"') + 2)
               and " " not in result[key]):
                result[key] = str(result[key].replace("_", " "))[1:-1]
            else:
                print(f"Error in string format for {result[key]}")
                return None
        return result

    def do_show(self, line):
        """
            Prints the __dict__ of an instance
            Usage: show <ClassName> <id>

            **Arguments**
               ClassName: required
               id: required
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = f"{args[0]}.{args[1]}"
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """
            Destroy an instance
            Usage: destroy <ClassName> <id>

            **Arguments**
               ClassName: required
               id: required
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = f"{args[0]}.{args[1]}"
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """
        Print all objects or all object for a class
        Usage: all [<ClassName>]

        **Arguments**
            ClassName: not required, a valid class name
        """
        args = parse(line)
        if len(line) == 0:
            obj_l = [objs for objs in storage.all().values()]
            print(obj_l)
        elif args[0] in HBNBCommand.classes.keys():
            obj_l = [objs for key, objs in storage.all().items()
                     if args[0] in key]
            print(obj_l)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates a valid object by changing or creating authorized attributes.
        Usage: update <class name> <id> <attribute name> <attribute value>

        **Arguments**
            class name: class name of the object
            id: unique user id of the object
            attribute name: name of attribute to change or create
            attribute value: value of attribute
        """
        args = parse(line)
        if len(args) >= 4:
            key = f"{args[0]}.{args[1]}"
            for k, v in storage.all().items():
                if k == key:
                    setattr(v, args[2], args[3])
                    storage.save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif (f"{args[0]}.{args[1]}") not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """
            Display count of instances specified : count User
        """
        if line in HBNBCommand.classes.keys():
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default_exec(self, cls, line):
        """
        Wrapper fnc for <ClassName>.action()
        """
        if line[:6] == '.all()':
            self.do_all(cls)
        elif line[:6] == '.show(':
            self.do_show(cls)
        elif line[:8] == '.count()':
            objects = {k: v for k, v in storage.all().items()
                       if isinstance(v, eval(cls))}
            print(len(objects))
        elif line[:9] == '.destroy(':
            self.do_destroy(f"{cls} {line[10: -2]}")
        elif line[:8] == '.update(':
            if '{' in line and '}' in line:
                arg = line[8:-1].split('{')
                arg[1] = '{' + arg[1]
            else:
                arg = line[8:-1].split(',')
            if len(arg) == 3:
                arg = " ".join(arg)
                arg = arg.replace('"', '').replace('  ', ' ')
                self.do_update(f"{cls} {arg}")
            elif len(arg) == 2:
                try:
                    dictionary = eval(arg[1])
                except Exception:
                    return
                for i in dictionary.keys():
                    s = f"{cls} {arg[0][1:-3]} {str(i)} {str(dictionary[i])}"
                    self.do_update(s)
            else:
                return
        else:
            print("Not a valid command")

    def do_BaseModel(self, line):
        """
        **Usage**
        BaseModel.all(), BaseModel.count(), BaseModel.show(<id>),
        BaseModel.destroy(<id>),
        BaseModel.update(<id>, <attribute name>, <attribute value>)
        BaseModel.update(<id>, <dictionary of attributes and values>)
        """
        self.default_exec('BaseModel', line)

    def do_User(self, line):
        """
        **Usage**
        User.all(), User.count(), User.show(<id>),  User.destroy(<id>),
        User.update(<id>, <attribute name>, <attribute value>)
        User.update(<id>, <dictionary of attributes and values>)
        """
        self.default_exec('User', line)

    def do_City(self, line):
        """
        **Usage**
        City.all(), City.count(), City.show(<id>),  City.destroy(<id>),
        City.update(<id>, <attribute name>, <attribute value>)
        City.update(<id>, <dictionary of attributes and values>)
        """
        self.default_exec('City', line)

    def do_State(self, line):
        """
        **Usage**
        State.all(), State.count(), State.show(<id>),  State.destroy(<id>),
        State.update(<id>, <attribute name>, <attribute value>)
        State.update(<id>, <dictionary of attributes and values>)
        """
        self.default_exec('State', line)

    def do_Place(self, line):
        """
        **Usage**
        Place.all(), Place.count(), Place.show(<id>),  Place.destroy(<id>),
        Place.update(<id>, <attribute name>, <attribute value>)
        Place.update(<id>, <dictionary of attributes and values>)
        """
        self.default_exec('Place', line)

    def do_Amenity(self, line):
        """
        **Usage**
        Amenity.all(), Amenity.count(), Amenity.show(<id>),
        Amenity.destroy(<id>),
        Amenity.update(<id>, <attribute name>, <attribute value>)
        Amenity.update(<id>, <dictionary of attributes and values>)
        """
        self.default_exec('Amenity', line)

    def do_Review(self, line):
        """
        **Usage**
        Review.all(), Review.count(), Review.show(<id>),  Review.destroy(<id>),
        Review.update(<id>, <attribute name>, <attribute value>)
        Review.update(<id>, <dictionary of attributes and values>)
        """
        self.default_exec('Review', line)


def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
