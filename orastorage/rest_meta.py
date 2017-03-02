import re

ORACLOUD_STORAGE_STEC = {
    'identity':{
        'authenticate a user': {
            'task': 'idnetity',
            'api_name': 'Authenticate a user',
            'path': '/auth/v1.0/',
            'method': 'GET',
            'query params': [],
            'request headers': [
                'X-Auth-Key',
                'X-Auth-User'
            ],
            'response headers': [
                'Content-Length',
                'Content-Type',
                'Date',
                'X-Auth-Token',
                'X-Storage-Token',
                'X-Storage-Url',
                'X-Trans-Id'
            ],
            'success_status_codes': [200],
            'fail_status_codes': [401]
        }
    },
    'accounts':{
        'manage account metadata': {
            'task': 'accounts',
            'api_name': 'manage account metadata',
            'path': '/v1/{account}',
            'method': 'POST',
            'query params': ['bulk-delete'],
            'request headers': [
                'X-Account-Meta-Temp-URL-Key',
                'X-Account-Meta-Temp-URL-Key-2',
                'X-Account-Meta-{name}',
                'X-Auth-Token'
            ],
            'response headers': [],
            'success_status_codes': [204],
            'fail_status_codes': [401]
        },
        'bulk delete':{
            'path': '/v1/{account}',
            'method': 'GET',
            'query param': ['delimiter', 'end_marker', 'format',
                                'limit', 'marker', 'prefix'],
            'request header': ['Accept', 'X-Auth-Token', 'X-Newest'],
            'response header': ['Content-Length', 'Content-Type', 'Date', 'X-Account-Bytes-Used',
                                'X-Account-Container-Count', 'X-Account-Meta-Temp-URL-Key',
                                'X-Account-Meta-Temp-URL-Key-2', 'X-Account-Meta-name',
                                'X-Account-Object-Count', 'X-Timestamp', 'X-Trans-Id'],
            'success_status_codes': [200],
            'fail_status_codes': [204, 401]
        },
        'show account details':{
            'task': 'accounts',
            'api_name': 'show account details',
            'path': '/v1/{account}',
            'method': 'GET',
            'query params': ['delimiter', 'end_marker', 'format',
                            'limit', 'marker', 'prefix'],
            'request headers': ['Accept', 'X-Auth-Token', 'X-Newest'],
            'response headers': ['Content-Length', 'Content-Type', 'Date', 'X-Account-Bytes-Used',
                                'X-Account-Container-Count', 'X-Account-Meta-Temp-URL-Key',
                                'X-Account-Meta-Temp-URL-Key-2', 'X-Account-Meta-name',
                                'X-Account-Object-Count', 'X-Timestamp', 'X-Trans-Id'],
            'success_status_codes': [200],
            'fail_status_codes': [204, 401]
        },
        'show account metadata': {
            'task': 'accounts',
            'api_name': 'Show account metadata',
            'path': '/v1/{account}',
            'method': 'HEAD',
            'query params': [],
            'request headers': ['X-Auth-Token', 'X-Newest'],
            'response headers': ['Content-Length', 'X-Account-Bytes-Used', 'X-Account-Container-Count',
                                'X-Account-Meta-Temp-URL-Key', 'X-Account-Meta-Temp-URL-Key-2',
                                'X-Account-Meta-{name}', 'X-Account-Object-Count', 'X-Timestamp',
                                'X-Trans-Id'],
            'success_status_codes': [204],
            'fail_status_codes': [401]
        }
    },
    'bulk operations':{
        'delete multiple containers or objects': {
            'path': '/v1/{account}',
            'request header': ['Accept','Content-Length', 'Content-Type', 'X-Auth-Token'],
            'body': ['Errors', 'Number Deleted', 'Number Not Found', 'Response Body', 'Response Status'],
            'success_status_codes': [200]
        }
    },
    'containers': {
        'create container': {
            'task': 'containers',
            'api_name': 'create container',
            'path': '/v1/{account}/{container}',
            'method': 'PUT',
            'query params': ['extract-archive'],
            'request headers': [
                'X-Auth-Token',
                'X-Container-Meta-Access-Control-Allow-Origin',
                'X-Container-Meta-Access-Control-Expose-Headers',
                'X-Container-Meta-Access-Control-Max-Age,'
                'X-Container-Meta-Temp-URL-Key',
                'X-Container-Meta-Temp-URL-Key-2',
                'X-Container-Meta-{name}',
                'X-Container-Read',
                'X-Container-Write'
            ],
            'response headers': ['Content-Length',
                                 'Content-Type',
                                 'Date',
                                 'X-Timestamp',
                                 'X-Trans-Id'],
            'success_status_codes': [201, 202],
            'fail_status_codes': [401, 403]
        },
        'delete container': {
            'task': 'containers',
            'api_name': 'delete container',
            'path': '/v1/{account}/{container}',
            'method': 'DELETE',
            'query params': [],
            'request headers': [
                'X-Auth-Token',
                'X-Container-Meta-Temp-URL-Key',
                'X-Container-Meta-Temp-URL-Key-2'
            ],
            'response headers': ['Content-Length',
                                 'Date',
                                 'X-Timestamp',
                                 'X-Trans-Id'],
            'success_status_codes': [204],
            'fail_status_codes': [401,403,404,409]
        },
        'show container details and list objects': {
            'task': 'containers',
            'api_name': 'show container details and list objects',
            'path': '/v1/{account}/{container}',
            'method': 'GET',
            'query params': ['delimiter','end_marker','format','limit',
                             'marker','path','prefix'],
            'request headers': [
                'Accept',
                'X-Auth-Token',
                'X-Container-Meta-Temp-URL-Key',
                'X-Container-Meta-Temp-URL-Key-2',
                'X-Newest'
            ],
            'response headers': ['Accept-Ranges',
                                 'Content-Length',
                                 'Content-Type',
                                 'Date',
                                 'X-Container-Bytes-Used',
                                 'X-Container-Meta-Access-Control-Allow-Origin',
                                 'X-Container-Meta-Access-Control-Expose-Headers',
                                 'X-Container-Meta-Access-Control-Max-Age',
                                 'X-Container-Meta-Temp-URL-Key',
                                 'X-Container-Meta-Temp-URL-Key-2',
                                 'X-Container-Meta-{name}',
                                 'X-Container-Object-Count',
                                 'X-Timestamp','X-Trans-Id'],
            'success_status_codes': [200,204],
            'fail_status_codes': [401, 403, 404, 409]
        },
        'show container metadata': {
            'task': 'containers',
            'api_name': 'show container metas',
            'path': '/v1/{account}/{container}',
            'method': 'HEAD',
            'query params': [],
            'request headers': [
                'X-Auth-Token',
                'X-Container-Meta-Temp-URL-Key',
                'X-Container-Meta-Temp-URL-Key-2',
                'X-Newest'
            ],
            'response headers': ['Accept-Ranges',
                                 'Content-Length',
                                 'Content-Type',
                                 'Date',
                                 'X-Container-Bytes-Used',
                                 'X-Container-Meta-Access-Control-Allow-Origin',
                                 'X-Container-Meta-Access-Control-Expose-Headers',
                                 'X-Container-Meta-Access-Control-Max-Age',
                                 'X-Container-Meta-Quota-Count',
                                 'X-Container-Meta-Quota-Bytes'
                                 'X-Container-Meta-Temp-URL-Key',
                                 'X-Container-Meta-Temp-URL-Key-2',
                                 'X-Container-Meta-{name}',
                                 'X-Container-Object-Count',
                                 'X-Container-Write',
                                 'X-Container-Read',
                                 'X-Timestamp',
                                 'X-Trans-Id'],
            'success_status_codes': [204],
            'fail_status_codes': [401, 403, 404]
        },

    },
    'discoverability':{
        'list activated capabilities':{
            'task': 'discoverability',
            'api_name': 'list activated capabilities',
            'path': '/info',
            'method': 'GET',
            'query params': [],
            'request headers': ['X-Auth-Token'],
            'response headers': ['Content-Length',
                                 'Content-Type',
                                 'Date',
                                 'ETag',
                                 'Last-Modified',
                                 'X-Timestamp',
                                 'X-Trans-Id'],
            'success_status_codes': [200],
            'fail_status_codes': []
        }
    },
    'objects':{
        'create or replace object': {
            'task': 'objects',
            'api_name': 'create or replace object',
            'path': '/v1/{account}/{container}/{object}',
            'method': 'PUT',
            'query params': ['multipart-manifest', 'temp_url_expires', 'temp_url_sig'],
            'request headers': [
                'Content-Disposition', 'Content-Encoding',
                'Content-Length', 'Content-Type','ETag',
                'If-None-Match', 'Transfer-Encoding', 'X-Auth-Token'
                'X-Copy-From', 'X-Delete-After', 'X-Delete-At', 'X-Object-Meta-{name}'
            ],
            'response headers': ['Content-Length',
                                 'Content-Type',
                                 'Date', 'ETag', 'Last-Modified',
                                 'X-Timestamp',
                                 'X-Trans-Id'],
            'success_statuscodes': [201, 202],
            'fail_statuscodes': [401, 403, ]
        },
        'create or update object metadata': {},
        'delete object': {
            'task': 'objects',
            'api_name': 'delete object',
            'path': '/v1/{account}/{container}/{object}',
            'method': 'DELETE',
            'query params': ['multipart-manifest'],
            'request headers': ['X-Auth-Token'],
            'response headers': ['Content-Length',
                                 'Content-Type',
                                 'Date',
                                 'X-Timestamp',
                                 'X-Trans-Id'],
            'success_status_codes': [204],
            'fail_status_codes': [401, 403, 404]
        },
        'Get object content and metadata': {},
        'Show object metadata': {}
    }
}


class ApiSpec:
    def __init__(self, spec):
        if spec is None or not isinstance(spec, dict):
            raise TypeError("sepc parameter shoud be dict type")
        if spec.get('method').islower():
            raise ValueError('method should be uppercase in %s, %s' %
                             (spec.get('task'), spec.get('api_name')))

        self._task = spec.get('task')
        self._api_name = spec.get('api_name')
        self._path = spec.get('path')
        self._method = spec.get('method')
        self._query_params = spec.get('query params')
        self._request_headers = spec.get('request headers')
        self._response_headers = spec.get('response headers')
        self._success_status_codes = spec.get('success_status_codes')
        self._fail_status_codes = spec.get('fail_status_codes')

    def __str__(self):
        output = ['task: %s:' % self._task,
                  'api name: %s' % self._api_name,
                  'path: %s:' % self._path,
                  'method: %s:' % self._method,
                  'query_params: %s' % self._query_params,
                  'request headers: %s' % self._request_headers,
                  'response headers: %s' % self._response_headers,
                  'success status code: %s' % self._success_status_codes,
                  'Fail status codes: %s' % self._fail_status_codes]
        return '\n'.join(output)

    def get_success_statuscodes(self):
        return self._success_status_codes

    def get_fail_statuscodes(self):
        return self._fail_status_codes

    def get_task(self):
        return self._task

    def get_api_name(self):
        return self._api_name

    def get_path(self):
        return self._path

    def get_method(self):
        return self._method

    def get_query_params(self):
        return self._query_params

    def get_request_headers(self):
        return self._request_headers

    def get_response_headers(self):
        return self._response_headers

    def exists_placeholder_in_path(self):
        placeholders = re.findall(r'{\w+}', self.get_path())
        return len(placeholders)>0


def load_apispec(task, api_name):
    global ORACLOUD_STORAGE_STEC
    try:
        spec = ORACLOUD_STORAGE_STEC[task.lower()][api_name.lower()]
    except KeyError:
        raise ValueError("please check task and api_name. Target API Spec is not exist.(%s,%s)" %
                         (task, api_name))
    else:
        return ApiSpec(spec)