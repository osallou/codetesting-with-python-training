from nose.tools import *
from nose.plugins.attrib import attr


from mysamplecode.samplecode import SampleCode
import mock
from mock import patch
import logging

import unittest

class MockLdapConn(object):

  ldap_user = 'sampleuser'
  ldap_user_email = 'ldap@no-reply.org'

  STRATEGY_SYNC = 0
  AUTH_SIMPLE = 0
  STRATEGY_SYNC = 0
  STRATEGY_ASYNC_THREADED = 0
  SEARCH_SCOPE_WHOLE_SUBTREE = 0
  GET_ALL_INFO = 0

  @staticmethod
  def Server(ldap_host, port, get_info):
      return None

  @staticmethod
  def Connection(ldap_server, auto_bind=True, read_only=True, client_strategy=0, user=None, password=None, authentication=0,check_names=True):
      if user is not None and password is not None:
          if password == 'notest':
              #raise ldap3.core.exceptions.LDAPBindError('no bind')
              return None
      return MockLdapConn(ldap_server)

  def __init__(self, url=None):
    pass

  def search(self, base_dn, filter, scope, attributes=[]):
    if MockLdapConn.ldap_user in filter:
      self.response = [{'dn': MockLdapConn.ldap_user, 'attributes': {'mail': [MockLdapConn.ldap_user_email]}}]
      return [(MockLdapConn.ldap_user, {'mail': [MockLdapConn.ldap_user_email]})]
    else:
      raise Exception('no match')

  def unbind(self):
    pass



class Test(unittest.TestCase):


    def setUp(self):
        self.counter = 0

    def tearDown(self):
        pass

    @attr('count')
    def testAdd(self):
        sample = SampleCode()
        result = sample.add(1,1)
        self.assertEqual(2, result)

    @patch('ldap3.Connection')
    def testAuthenticate(self, initialize_mock):
        mockldap = MockLdapConn()
        initialize_mock.return_value = MockLdapConn.Connection(None, None, None, None)
        sample = SampleCode()
        is_auth = sample.authenticate('sampleuser', 'yy')
