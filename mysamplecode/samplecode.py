import os
import logging


class SampleCode(object):

    def __init__(self):
        pass


    def authenticate(self, login, password):
        '''
        Checks user credentials

        :return: bool
        '''
        from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO
        ldap_server = Server('localhost', port = 3890, get_info = GET_ALL_INFO)
        con = Connection(ldap_server, auto_bind = True, client_strategy = STRATEGY_SYNC, check_names=True)
        base_dn = 'ou=People,dc=genouest,dc=org'
        ldap_filter =  "(&(|(uid=" + login + ")(mail=" + login + ")))"
        attrs = ['mail']
        con.search(base_dn, ldap_filter, SEARCH_SCOPE_WHOLE_SUBTREE, attributes=attrs)
        # We would bind to check password .....
        if login == 'sampleuser':
            return True
        else:
            return False


    def add(self, input1, input2):
        '''
        Adds input1 and input2. In case of error, return -1
        '''
        result = -1
        try:
            result = input1+input2
        except Exception as e:
            logging.error(str(e))
        return result
