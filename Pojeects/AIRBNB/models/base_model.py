#!/usr/bin/python3
import uuid
from datetime import datetime
import  models

class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}" 
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"]= self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
