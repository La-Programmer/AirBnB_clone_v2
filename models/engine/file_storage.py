#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            result = {}
            for i in FileStorage.__objects:
                object = i.split('.')
                if cls.__name__ == object[0]:
                    result[i] = FileStorage.__objects[i]
            return result

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # print(f'New object: {obj.__class__.__name__}.{obj.id}: {obj}')
        self.all().update({obj.__class__.__name__ + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            # print("File Storage Objects: {}".format(FileStorage.__objects))
            temp.update(self.__objects)
            # print("Object to save: {}".format(self))
            # print("Trying to see temp: {}".format(temp))
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from storage"""
        if obj:
            if obj in FileStorage.__objects.values():
                del FileStorage.__objects['{}.{}'.format
                                          (obj.__class__.__name__, obj.id)]
    
    def close(self):
        """Deserializes JSON file to objects"""
        self.reload()
