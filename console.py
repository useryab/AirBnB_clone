#!/usr/bi/python3
"""
The console
contains
"""
import cmd
import json
import re
import models
# from models
from models.base_model import Basemodel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class (cmd.Cmd):
    """
    Console class
    """
