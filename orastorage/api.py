from orastorage.rest_identity import authenticate_a_user
from orastorage.exceptions import AuthorizationException
import requests

def get_token(user_id, password, idnetity_domain):
    try:
        response = authenticate_a_user(user_id=user_id,
                                       password=password,
                                       identity_domain=idnetity_domain)
    #except requests.HTTPError as http_error:
    #    pass
    except requests.ConnectionError as conn_error:
        if conn_error.response.status_code == 401 :
            raise AuthorizationException(
                "Incorrect user_id or password. (user_id, password)=(%s, %s)" % (user_id, password) )
        else:
            raise Exception(conn_error.message)
    else:
        return response.headers['X-Auth-Token']

