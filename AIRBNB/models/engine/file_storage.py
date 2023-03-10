#!/usr/bin/python3
import json
class FileStorage():
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return self.__objects
	def new(self, obj):
		key = ("{} {}".format(self.__class__.__name__, self.id))
		self.__objects[key] = obj
	def save(self):
		with open(self.__file_path, "w", encoding="utf-8") as f:
			p = {k: v.to_dict() for k, v in self.__objects.items()}
			json.dump(p, f)
	def reload(self):
		try:
			with open(self.__file_path, "r", encoding="utf-8") as f:
				p_dict = json.load(f)
				p_dict = eval(self.__class__.__name__(p_dict))
		except:
			pass



