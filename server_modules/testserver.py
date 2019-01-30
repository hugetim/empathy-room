import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.email
import anvil.tables as tables
from anvil.tables import app_tables
import anvil.users
import anvil.server
import parameters as p
import matcher
import datetime


@anvil.server.callable
@anvil.tables.in_transaction
def test_add_user(em, level=1, r_em=False, m_em=False):
  assert anvil.server.session['user']['trust_level'] >= p.TEST_TRUST_LEVEL
  if not anvil.server.session['test_record']:
    anvil.server.session['test_record'] = create_tests_record()
  new_user = app_tables.users.add_row(email=em,
                                      enabled=True,
                                      trust_level=level,
                                      request_em=r_em,
                                      match_em = m_em
                                     )
  test_users = anvil.server.session['test_record']['test_users']
  anvil.server.session['test_record']['test_users'] = test_users + [new_user]
  return new_user.get_id()


@anvil.server.callable
@anvil.tables.in_transaction
def test_add_request(user_id, request_type = "will_offer_first"):
  assert anvil.server.session['user']['trust_level'] >= p.TEST_TRUST_LEVEL
  if not anvil.server.session['test_record']:
    anvil.server.session['test_record'] = create_tests_record()
  user = app_tables.users.get_by_id(user_id)
  matcher.add_request(user_id, request_type)
  new_row = app_tables.requests.get(user=user, current=True)
  assert new_row # fails if match commenced instantly
  test_requests = anvil.server.session['test_record']['test_requests']
  anvil.server.session['test_record']['test_requests'] = test_requests + [new_row]
  return new_row


def create_tests_record():
  return app_tables.test_data.add_row(test_users = [],
                                      test_requests = []
                                     )


@anvil.server.callable
@anvil.tables.in_transaction
def test_clear():
  assert anvil.server.session['user']['trust_level'] >= p.TEST_TRUST_LEVEL
  test_records = app_tables.test_data.search()
  for row in test_records:  
    for user in row['test_users']:
      user.delete()
    for request in row['test_requests']:
      request.delete()                              
    row.delete()
  anvil.server.session['test_record'] = None
    

@anvil.server.callable
def test_get_user_list():
  assert anvil.server.session['user']['trust_level'] >= p.TEST_TRUST_LEVEL
  users = app_tables.users.search()
  to_return = []
  for user in users:
    to_return += [(user['email'], user.get_id())]
  return to_return
