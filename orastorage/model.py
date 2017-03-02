# -*- coding: utf-8 -*-
from __future__ import absolute_import


class Identity:
    """
    - 사용자 정보
    - Account 정보를 이용하여 인증을 수행
    """

    def __init__(self, identity_domain, user_id, password=None):
        self._identity_domain = identity_domain
        self._user_id = user_id
        self._password = password
        self._rest_endpoint = 'https://%s.storage.oraclecloud.com' % identity_domain
        self._storage_user = 'Storage-%s:%s' % (identity_domain, user_id)
        self._account = 'Storage-%s' % identity_domain

    def __str__(self):
        contents = ['Identity domain: %s' % self._identity_domain,
                    'user id: %s' % self._user_id,
                    'Is password saved?: %s' % (self._password is not None),
                    'REST endpoint: %s' % self._rest_endpoint,
                    'Storage user: %s' % self._storage_user,
                    'Account: %s' % self._account]

        return '\n'.join(contents)

    def get_rest_endpoint(self):
        return self._rest_endpoint

    def get_identity_domain(self):
        return self._identity_domain

    def get_password(self):
        return self._password

    def get_storage_user(self):
        return self._storage_user

    def get_user_id(self):
        return self._user_id

    def get_account(self):
        return self._account
