#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "
	__classes = {"BaseModel"}
	def do_quit(self, line):
		"""Quit command to exit console 
		"""

		return True
	def do_EOF(self, line):
		""""Signal to exit program
		"""

		return True
	def emptyline(self):
		return
	def do_create(self, line):
		args = line.split()
		if len(args) == 0:
			print("** class name missing **")
		elif args[0] not in (self.__classes):
			print("** class doesn't exist")
		else:
		 new_instance = eval(f"{args[0]}")()
		 print(new_instance.id)
		 
		     


if __name__ == '__main__':
    HBNBCommand().cmdloop()
