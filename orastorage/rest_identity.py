from orastorage.common import invoke_rest_api
from orastorage.model import Identity
TASK = 'identity'


def authenticate_a_user(user_id, password, identity_domain):
    """
    :param user_id: 
    :param password: 
    :param identity_domain: 
    :return: 
    """
    global TASK
    api_name = 'Authenticate a user'

    identity = Identity(identity_domain=identity_domain,
                        user_id=user_id,
                        password=password)

    headers = dict()
    headers['X-Auth-User'] = identity.get_storage_user()
    headers['X-Auth-Key'] = identity.get_password()

    response = invoke_rest_api(TASK, api_name,
                               identity.get_identity_domain(),
                               headers)
    return response
