from __future__ import absolute_import
import unittest
from tests.util import get_target_dir_for_test
from tests.util import get_login_info
from tests.util import remove_login_info
from tests.util import get_identity
import os


class TestUtilConfigFile(unittest.TestCase):
    def test_data_dir(self):
        target_dir = get_target_dir_for_test()
        self.assertTrue('-py/target' in target_dir)
        self.assertTrue(os.path.isdir(target_dir))
        self.assertTrue(os.path.exists(target_dir))

    def test_cached_login_info(self):
        login_ini = get_login_info()
        target_dir = get_target_dir_for_test()
        self.assertTrue(os.path.exists(target_dir+'/cache_orastorage.ini'))

        self.assertTrue("@" in login_ini.get('login', 'user_id'))
        self.assertTrue(login_ini.get('login', 'password') is not None)
        self.assertTrue(login_ini.get('login', 'identity_domain') is not None)

        remove_login_info()
        self.assertFalse(os.path.exists(target_dir + '/cache_orastorage.ini'))

    def test_get_identity(self):
        remove_login_info()
        login_info = get_login_info()
        identity = get_identity()
        self.assertEqual(identity.get_password(), login_info.get('login', 'password'))
        self.assertEqual(identity.get_user_id(), login_info.get('login', 'user_id'))
        self.assertEqual(identity.get_identity_domain(), login_info.get('login', 'identity_domain'))


