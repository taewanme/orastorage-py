import unittest
from tests.util import get_data_dir_for_test
import os
import ConfigParser

class TestUtilConfigFile(unittest.TestCase):
    def test_data_dir(self):
        test_dir = get_data_dir_for_test()
        self.assertTrue('oracloud-storage-py/tests/data' in test_dir)
        self.assertTrue(os.path.isdir(test_dir))
        self.assertTrue(os.path.exists(test_dir))

    def test_save_ini(self):
        #basedir = get_data_dir_for_test()
        section = 'login'

        account = ConfigParser.ConfigParser()
        account.add_section(section)

        user_id = os.environ.get("user_id")
        password = os.environ.get("passowrd")
        identity_domain = os.environ.get("domain")

        account.set(section, 'user_id', user_id)
        account.set(section, 'password', password)
        account.set(section, 'domain', identity_domain)











