from orastorage.rest_identity import authenticate_a_user
from orastorage.exceptions import AuthorizationException
from orastorage.exceptions import REST401Exception
from orastorage.exceptions import RESTOtherStatusException
from orastorage.exceptions import NetworkException
import requests


def get_token(user_id, password, idetity_domain):
    try:
        response = authenticate_a_user(user_id=user_id,
                                       password=password,
                                       identity_domain=idetity_domain)

    except requests.ConnectionError as e:
        raise NetworkException(message='please check network status and identity_domain information '
                                       '(entered Identity domain:%s)' % idetity_domain,
                               origin_message=e.message)
    except REST401Exception:
        raise AuthorizationException(
            "Incorrect user_id or password. (user_id, password)=(%s, %s)" % (user_id, password))
    except RESTOtherStatusException as e:
        raise Exception("Unsupported error. please send error message to orastorage-py", e.message)
    else:
        return response.headers.get('X-Auth-Token')

