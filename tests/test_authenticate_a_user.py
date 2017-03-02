from unittest import TestCase
from orastorage.rest_identity import authenticate_a_user
from orastorage.exceptions import *
from tests.util import get_identity
from orastorage.model import Identity
from requests import HTTPError
from requests import ConnectionError


class TestAuthenticate_a_user(TestCase):
    def test_authenticate_a_user(self):
        identity = get_identity()

        response = authenticate_a_user(identity.get_user_id(),
                                       identity.get_password(),
                                       identity.get_identity_domain())
        self.assertTrue(response.headers.get('X-Storage-Token') is not None)
        token = response.headers.get('X-Storage-Token')
        self.assertTrue('AUTH_' in token)

    def test_test_authenticate_a_user_with_invalid_password(self):
        identity = get_identity()
        invalid_identity = Identity(identity.get_identity_domain(),
                                    identity.get_user_id(),
                                    identity.get_password()+'1')
        with self.assertRaises(REST401Exception) as context:
            authenticate_a_user(invalid_identity.get_user_id(),
                                invalid_identity.get_password(),
                                invalid_identity.get_identity_domain())

    def test_test_authenticate_a_user_with_invalid_id(self):
        identity = get_identity()
        invalid_identity = Identity(identity.get_identity_domain(),
                                    identity.get_user_id()+'1',
                                    identity.get_password())
        with self.assertRaises(REST401Exception) as context:
            authenticate_a_user(invalid_identity.get_user_id(),
                                invalid_identity.get_password(),
                                invalid_identity.get_identity_domain())

    def test_test_authenticate_a_user_with_invalid_domain(self):
        identity = get_identity()
        invalid_identity = Identity(identity.get_identity_domain()+'1',
                                    identity.get_user_id(),
                                    identity.get_password())
        with self.assertRaises(ConnectionError) as context:
            authenticate_a_user(invalid_identity.get_user_id(),
                                invalid_identity.get_password(),
                                invalid_identity.get_identity_domain())

        print(context.exception)
        print(context.exception.strerror)


