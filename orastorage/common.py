# -*- coding: utf-8 -*-

from requests.packages.urllib3.exceptions import SubjectAltNameWarning
from requests.packages.urllib3.exceptions import SNIMissingWarning
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
import requests
from rest_meta import load_apispec
import re



def invoke_rest_api(task, api_name, identity_domain, headers_meta=None, url_metas=None, data=None):
    """
    
    :param task: 
    :param api_name: 
    :param identity_domain: 
    :param headers_meta: 
    :param url_metas: 
    :param data: 
    :return: 
    """
    requests.packages.urllib3.disable_warnings(SubjectAltNameWarning)
    requests.packages.urllib3.disable_warnings(SNIMissingWarning)
    requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
    # http://stackoverflow.com/questions/28707134/why-request-with-ssl-certification-returns-html 
    #  ignoring warning message 
    #  Warning messages are appeared with old urllib3 version 

    if data is not None and not isinstance(data, str):
        if isinstance(data, dict):
            raise ValueError('data should be processed with json.dumps()')

    spec = load_apispec(task, api_name)

    if spec.exists_placeholder_in_path() and url_metas is None:
        message = "url_meta should be inputted when path parameter is contained in rest path"
        raise ValueError(message)

    if headers_meta is not None and not isinstance(headers_meta, dict):
        raise TypeError("headers_meta parameter should be dict type")

    headers = {}
    for k, v in headers_meta.items():
        headers[k] = v

    url = gen_url(get_rest_end_point(identity_domain), spec.get_path(), url_metas)

    response = None

    if spec.get_method() == "GET":
        response = requests.get(url=url, headers=headers)
    elif spec.get_method() == "HEAD":
        response = requests.head(url=url, headers=headers)
    elif spec.get_method() == "POST":
        response = requests.post(url=url, headers=headers, data=data)
    elif spec.get_method() == "PUT":
        response = requests.put(url=url, headers=headers, data=data)
    elif spec.get_method() == "DELETE":
        response = requests.delete(url=url, headers=headers)

    return response



def gen_url(url, path, url_metas=None):
    """
    
    :param url: 
    :param path: 
    :param url_metas: 
    :return: 
    """
    rest_url = url + path
    ## todo: rest_url의 double slash 이슈를 해결해야 함

    placeholders = re.findall(r'{\w+}', rest_url)

    for tag in placeholders:
        key = tag[1:len(tag)-1] #extrace key
        if isinstance(url_metas[key], str):
            value = url_metas[key]
        else:
            value = str(url_metas[key])

        rest_url = rest_url.replace(tag, value) #replace

    return rest_url


def get_rest_end_point(identity_domain):
    return 'https://%s.storage.oraclecloud.com' % identity_domain


