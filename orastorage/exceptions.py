class BaseException(Exception):
    def __init__(self, message, reason=None, origin_message=None, headers=None):
        self.message = message
        self.reason = reason
        self.origin_message = origin_message
        self.headers = headers

    def __str__(self):
        ret = "[Oracle_Storage_Exception] %s\n" % str(self.message)
        if self.reason is not None:
            ret += "[REASON] %s\n" % str(self.reason)
            ret += "[Origin Message] %s\n" % str(self.origin_message)
        return ret


class AuthorizationException(BaseException):
    """ Error in authorization with information(ID, password and domain) for retrieving Access-Token
    """
    status_code = 401
    desc = "Unauthorized"


class InvalidTokenException(BaseException):
    """Request does not include an access token or have an invalid access token."""
    status_code = 401
    desc = """
    Request does not include an authentication token, or authentication token specified
    in the request is not valid. It may have expired.
    Authentication tokens expire after 30 minutes.
    """


class ForbiddenException(BaseException):
    status_code = 403
    desc = """
    Forbidden. Possible causes:
    - A data center has not been selected for your service in Oracle Cloud My Services.
    - The request was sent to an incorrect data center.
      - For example, the data center for your service is Chicago (us2),
      - but the request was sent to the URL corresponding to the Ashburn (us6) data center.
    - You don't have the required permission to perform the operation on the specified container.
      - For example,
        - there may be a change in the roles assigned to your user
        - the access privileges defined for the container specified in the request.
    - The specified operation is not permitted for archive objects or containers with storage class Archive
    """


class ObjectNotFoundException(BaseException):
    desc = """The container does not exist or has just been created and hasn't been replicated
    across all three nodes."""
    status_code = 404


class RequestTimeoutException(BaseException):
    desc = """Request Timeout"""
    status_code = 408


class IncompleteObjectException(BaseException):
    desc = """
    The object does not exist or has just been created and hasn't been replicated across all three nodes.
    """
    status_code = 416


class IncompleteHeaderException(BaseException):
    desc = "Request is missing either a Transfer-Encoding or a Content-Length header"
    status_code = 411


class ExcessOfLimitException(BaseException):
    desc = """
    The operation exceeds one of the following limits:
      - Object size greater than 5GB
      - Additional object data exceeds the unused quota on the account
      - (If container quotas are set) Additional object data or number of objects 
        exceeds the unused quota on the container.
    """
    status_code = 413


class ChecksumException(BaseException):
    desc = """The value of the ETag header specified in the upload request doesn't
    match the MD5 checksum of the HTTP response."""
    status_code = 422


class UnretrievedAchiveObjectException(BaseException):
    status_code = 400
    desc = """Must retrieve an archived object before downloading it."""


class OutOfRangeException(BaseException):
    status_code = 416
    desc = """Returned for any ranged GET requests that specify more than:
    - Fifty ranges
    - Three overlapping ranges
    - Eight non-increasing ranges"""


class NetworkException(BaseException):
    desc = """Connection Error in cloud storage server"""


class IncompleteInputException(Exception):
    """Incomplete Input Exception"""


class InvalidcommandException(Exception):
    """Invalid CLI Command"""


class UnloginedException(Exception):
    """Unloaded Exception"""


class NoSupportSubcommandException(Exception):
    """NoSupportSubcommandException"""


class NoSupportOperationException(Exception):
    """NoSupportOperationException"""


class REST401Exception(Exception):
    def __init__(self, *args):
        self.message = ''
        if len(args) > 0:
            self.message = args[0]
        Exception.__init__(self, *args)

    def __str__(self):
        return repr('REST 401 Exception : ' + self.message)


class REST403Exception(Exception):
    def __init__(self, *args):
        self.message = ''
        if len(args) > 0:
            self.message = args[0]
        Exception.__init__(self, *args)

    def __str__(self):
        return repr('REST 403 Exception : ' + self.message)


class REST404Exception(Exception):
    def __init__(self, *args):
        self.message = ''
        if len(args) > 0:
            self.message = args[0]
        Exception.__init__(self, *args)

    def __str__(self):
        return repr('REST 404 Exception : ' + self.message)


class REST409Exception(Exception):
    def __init__(self, *args):
        self.message = ''
        if len(args) > 0:
            self.message = args[0]
        Exception.__init__(self, *args)

    def __str__(self):
        return repr('REST 409 Exception : ' + self.message)

class RESTOtherStatusException(Exception):
    def __init__(self, *args):
        self.message = ''
        if len(args) > 0:
            self.message = args[0]
        Exception.__init__(self, *args)

    def __str__(self):
        return repr('REST Unchecked Status Code Exception : ' + self.message)