import unittest

import nuklear


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertIsNotNone(nuklear.__metadata_version__, "Metadata Version is None")
        self.assertIsNotNone(nuklear.__title__, "Package Name is None")
        self.assertIsNotNone(nuklear.__version__, "Package Version is None")
        self.assertIsNotNone(nuklear.__summary__, "Package Summary is None")
        self.assertIsNotNone(nuklear.__author__, "Package Author is None")
        self.assertIsNotNone(nuklear.__maintainer__, "Package Maintainer is None")
        self.assertIsNotNone(nuklear.__license__, "Package License is None")
        self.assertIsNotNone(nuklear.__url__, "Package URL is None")
        self.assertIsNotNone(nuklear.__download_url__, "Package Download URL is None")
        self.assertIsNotNone(nuklear.__project_urls__, "Package Version is None")
        self.assertIsNotNone(nuklear.__copyright__, "Package Version is None")
        self.assertIsNotNone(nuklear.__data_dir__, "Package Version is None")


if __name__ == "__main__":
    unittest.main()
