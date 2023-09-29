#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "
	__classes = ["BaseModel", "User", "State","City", "Amenity", "Place","Review"]
	def do_quit(self, arg):
		"""Quit command to exit console 
		"""
		return True
	def do_EOF(self, arg):
		""""Signal to exit program
		"""
		return True
	def emptyline(self):
		""" Method called when an empty line is
		    entered in response to the prompt
        	"""
		return
	def do_create(self, arg):
		args = arg.split()
		if len(args) == 0:
			print("** class name missing **")
		elif args[0] not in (self.__classes):
			print("** class doesn't exist")
		else:
		 new_object = eval(f"{args[0]}")()
		 print(new_object.id)
		 storage.save()
	def do_show(self, arg):
		args = arg.split()

		if (len(args) == 0):
			print("** class name missing **")
		elif args[0] not in self.__classes:
		 	print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
		elif f"{args[0]}.{args[1]}" not in storage.all():
			print("** no instance found ")
		else:
			print(storage.all()[f"{args[0]}.{args[1]}"])
	def do_destroy(self, arg):
		args = arg.split()
		if (len(args) == 0):
			print("** class name missing **")
		elif (args[0] not in self.__classes):
			print("** class doesn't exist **")
		elif len(args) == 1:
		 	print("** instance id missing **")
		elif f"{args[0]}.{args[1]}" not in storage.all():
			print("** no instance found **")
		else:
			del storage.all()[f"{args[0]}.{args[1]}"]
		storage.save()
	def do_all(self,arg):
		args = arg.split()
		if (len(args) == 0):
			print([str(value) for value in storage.all().values()])
		elif (args[0] not in self.__classes):
			print("** class doesn't exist **")
		else: 
		 	print([str(v) for k, v in storage.all().items() if k.startswith(args[0])])
	def do_update(self, arg):
		args = arg.split()

		if(len(args)== 0):
			print("** class name missing **")
		elif (args[0] not in self.__classes):
			print("** class doesn't exist **")
		elif (len(args) == 1):
			print("** instance id missing **")
		elif f"{args[0]}.{args[1]}" not in storage.all():
			print("** no instance found **")
		elif (len(args) == 2):
			print("** attribute name missing **")
		elif (len(args) == 3):
			print("** value missing **")
		else:
			obj_class = args[0]
			obj_id = args[1]
			obj_key = obj_class + "." + obj_id
			obj = storage.all()[obj_key]
			attribute_name = args[2]
			attribute_value = args[3]
			if (attribute_value[0] == '"'):
				attribute_value = attribute_value[1:-1]
			if hasattr(obj, attribute_name):
				type_ = type(getattr(obj, attribute_name))
				if (type_ in [str, float, int]):
					attribute_value = type_(attribute_value)
					setattr(obj, attribute_name, attribute_value)
			else:
				setattr(obj, attribute_name, attribute_value)
			storage.save()
	
	def default(self,arg):
		args = arg.split(".")
		if (args[0] in self.__classes):
			if (args[1] == "all()"):
				self.do_all(args[0])
			elif (args[1] == "count()"):
				list_ = [v for k, v in storage.all().items() if k.startswith(arg[0])]
				print(len(list_))
			elif (args[1].startswith("show")):
				id_ = args[1].split('"')[1]
				self.do_show(f"{args[0]} {id_}")
			elif (args[1].startswith("destroy")):
				id_ = args[1].split('"')[1]
				self.do_destroy(f"{args[0]} {id_}")
			elif (args[1].startswith("update")):
				split_ = args[1].split('(')
				split_ = split_[1].split(')')
				if ('{') in split_[0]:
					id_strip = split_[0].split(', {')
					id_strip = id_strip[0].split(', {')
					id_ = id_strip[0].strip('"')
					split_ = '{' + (split_[0].split('{'))[1]
					dict_ = eval(split_.strip('"'))
					
					if type(dict_) == dict:
						for k, v in dict_.items():
							self.do_update(f"{args[0]} {id_} {k} {v}")
				else:
					split_ = split_[0].split(', ')
					id_ = split_[0].strip('"')
					attr_name = split_[1].strip('"')
					attr_value = split_[2].strip('"')
					self.do_update(f"{args[0]} {id_} {attr_name} {attr_value}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
