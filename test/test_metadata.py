import unittest

import package


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertIsNotNone(package.__metadata_version__, "Metadata Version is None")
        self.assertIsNotNone(package.__title__, "Package Name is None")
        self.assertIsNotNone(package.__version__, "Package Version is None")
        self.assertIsNotNone(package.__summary__, "Package Summary is None")
        self.assertIsNotNone(package.__author__, "Package Author is None")
        self.assertIsNotNone(package.__maintainer__, "Package Maintainer is None")
        self.assertIsNotNone(package.__license__, "Package License is None")
        self.assertIsNotNone(package.__url__, "Package URL is None")
        self.assertIsNotNone(package.__download_url__, "Package Download URL is None")
        # self.assertIsNotNone(package.__project_urls__, "Package Version is None")
        # self.assertIsNotNone(package.__copyright__, "Package Version is None")
        # self.assertIsNotNone(package.__data_dir__, "Package Version is None")


if __name__ == "__main__":
    unittest.main()
