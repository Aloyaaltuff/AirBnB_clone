##!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import storage

class BaseModel:
    """A base class for all other classes in the project"""

    def __init__(self, *args, **kwargs):

        if kwargs:

            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()


    def to_dict(self):
        dict_representation = self.__dict__.copy()
        dict_representation['__class__'] = self.__class__.__name__
        dict_representation['created_at'] = self.created_at.isoformat()
        dict_representation['updated_at'] = self.updated_at.isoformat()
        return dict_representation

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
