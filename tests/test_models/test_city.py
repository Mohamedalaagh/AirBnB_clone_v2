class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test instantiation of City class without arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance is stored in objects."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if id attribute is a public string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test if created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if updated_at attribute is a public datetime."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """Test if state_id attribute is a public class attribute."""
        cty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cty))
        self.assertNotIn("state_id", cty.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test if name attribute is a public class attribute."""
        cty = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cty))
        self.assertNotIn("name", cty.__dict__)

    def test_two_cities_unique_ids(self):
        """Test if two cities have unique ids."""
        cty1 = City()
        cty2 = City()
        self.assertNotEqual(cty1.id, cty2.id)

    def test_two_cities_different_created_at(self):
        """Test if two cities have different created_at datetime."""
        cty1 = City()
        sleep(0.05)
        cty2 = City()
        self.assertLess(cty1.created_at, cty2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test if two cities have different updated_at datetime."""
        cty1 = City()
        sleep(0.05)
        cty2 = City()
        self.assertLess(cty1.updated_at, cty2.updated_at)

    def test_str_representation(self):
        """Test the string representation of City instance."""
        dat = datetime.today()
        dat_repr = repr(dat)
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = dat
        cty_str = cty.__str__()
        self.assertIn("[City] (123456)", cty_str)
        self.assertIn("'id': '123456'", cty_str)
        self.assertIn("'created_at': " + dat_repr, cty_str)
        self.assertIn("'updated_at': " + dat_repr, cty_str)

    def test_args_unused(self):
        """Test instantiation of City class with unused arguments."""
        cty = City(None)
        self.assertNotIn(None, cty.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of City class with keyword arguments."""
        dat = datetime.today()
        dat_iso = dat.isoformat()
        cty = City(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(cty.id, "345")
        self.assertEqual(cty.created_at, dat)
        self.assertEqual(cty.updated_at, dat)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of City class with None keyword arguments."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)
class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        """Set up method for test cases."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Tear down method for test cases."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test if saving once updates the 'updated_at' attribute."""
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        self.assertLess(first_updated_at, cty.updated_at)

    def test_two_saves(self):
        """Test if saving twice updates the 'updated_at' attribute."""
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        second_updated_at = cty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cty.save()
        self.assertLess(second_updated_at, cty.updated_at)

    def test_save_with_arg(self):
        """Test saving with argument."""
        cty = City()
        with self.assertRaises(TypeError):
            cty.save(None)

    def test_save_updates_file(self):
        """Test if saving updates the file."""
        cty = City()
        cty.save()
        cty_id = "City." + cty.id
        with open("file.json", "r") as f:
            self.assertIn(cty_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test the type of the output from to_dict method."""
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict contains correct keys."""
        cty = City()
        self.assertIn("id", cty.to_dict())
        self.assertIn("created_at", cty.to_dict())
        self.assertIn("updated_at", cty.to_dict())
        self.assertIn("__class__", cty.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if to_dict contains added attributes."""
        cty = City()
        cty.middle_name = "Holberton"
        cty.my_number = 98
        self.assertEqual("Holberton", cty.middle_name)
        self.assertIn("my_number", cty.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in to_dict are strings."""
        cty = City()
        cty_dict = cty.to_dict()
        self.assertEqual(str, type(cty_dict["id"]))
        self.assertEqual(str, type(cty_dict["created_at"]))
        self.assertEqual(str, type(cty_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method."""
        dat = datetime.today()
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(cty.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the contrast between to_dict and dunder dict."""
        cty = City()
        self.assertNotEqual(cty.to_dict(), cty.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict method with argument."""
        cty = City()
        with self.assertRaises(TypeError):
            cty.to_dict(None)


if __name__ == "__main__":
    unittest.main()

