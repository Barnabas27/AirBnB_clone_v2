#!/usr/bin/python3
""" test for amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
from os import getenv

class test_Amenity(test_basemodel):
    """ amenity test class" """

    def __init__(self, *args, **kwargs):
        """init the test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
