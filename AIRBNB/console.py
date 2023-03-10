#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
