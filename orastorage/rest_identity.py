from orastorage.common import invoke_rest_api
from orastorage.model import Identity
from orastorage.common import load_apispec
from orastorage.exceptions import REST401Exception
from orastorage.exceptions import RESTOtherStatusException
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

    spec = load_apispec(TASK, api_name)

    http_status_code = response.status_code

    if http_status_code in spec.get_success_statuscodes():
        return response
    elif http_status_code in spec.get_fail_statuscodes():
        raise REST401Exception(response.text)
    else:
        raise RESTOtherStatusException(response.text)


