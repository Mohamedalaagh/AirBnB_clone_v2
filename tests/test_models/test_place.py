#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_description_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

class TestPlace_save(unittest.TestCase):
    """Unit tests for testing the save method of the Place class."""

    @classmethod
    def setUp(cls):
        """Set up the test environment."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test saving one instance of Place."""
        plac = Place()
        sleep(0.05)
        first_updated_at = plac.updated_at
        plac.save()
        self.assertLess(first_updated_at, plac.updated_at)

    def test_two_saves(self):
        """Test saving two instances of Place."""
        plac = Place()
        sleep(0.05)
        first_updated_at = plac.updated_at
        plac.save()
        second_updated_at = plac.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        plac.save()
        self.assertLess(second_updated_at, plac.updated_at)

    def test_save_with_arg(self):
        """Test saving Place instance with an argument."""
        plac = Place()
        with self.assertRaises(TypeError):
            plac.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file."""
        plac = Place()
        plac.save()
        placid = "Place." + plac.id
        with open("file.json", "r") as f:
            self.assertIn(placid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unit tests for testing the to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test the type of the returned dictionary."""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the dictionary contains the correct keys."""
        plac = Place()
        self.assertIn("id", plac.to_dict())
        self.assertIn("created_at", plac.to_dict())
        self.assertIn("updated_at", plac.to_dict())
        self.assertIn("__class__", plac.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the dictionary contains added attributes."""
        plac = Place()
        plac.middle_name = "Holberton"
        plac.my_number = 98
        self.assertEqual("Holberton", plac.middle_name)
        self.assertIn("my_number", plac.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes are converted to strings."""
        plac = Place()
        plac_dict = plac.to_dict()
        self.assertEqual(str, type(plac_dict["id"]))
        self.assertEqual(str, type(plac_dict["created_at"]))
        self.assertEqual(str, type(plac_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the to_dict method."""
        dt = datetime.today()
        plac = Place()
        plac.id = "123456"
        plac.created_at = plac.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(plac.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the difference between to_dict and __dict__."""
        plac = Place()
        self.assertNotEqual(plac.to_dict(), plac.__dict__)

    def test_to_dict_with_arg(self):
        """Test if to_dict method raises an error with an argument."""
        plac = Place()
        with self.assertRaises(TypeError):
            plac.to_dict(None)


if __name__ == "__main__":
    unittest.main()

