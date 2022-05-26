import unittest

import domain
import orm


class TestModels(unittest.TestCase):
    def test_user_not_cool(self):
        user = domain.User(first_name='some', last_name='name')

        self.assertFalse(user.cool)

    def test_user_made_cool(self):
        user = domain.User(first_name='some', last_name='name')
        user.make_cool()

        self.assertTrue(user.cool)

    def test_user_full_name(self):
        user = domain.User(first_name='some', last_name='name')

        self.assertEqual(user.full_name, ' '.join([user.first_name, user.last_name]))

    def test_user_can_have_addresses(self):
        user = domain.User(first_name='some', last_name='name')
        address = domain.Address(email='some@address.com')
        user.addresses.append(address)

        self.assertTrue(user.addresses)
        self.assertEqual(user.addresses[0].email, 'some@address.com')


class TestDB(unittest.TestCase):
    def setUp(self):
        self.session = orm.init_db()

    def tearDown(self):
        self.session.close()

    def test_persistence(self):
        user = domain.User(first_name='some', last_name='name')
        address = domain.Address(email='some@address.com')
        user.addresses.append(address)

        self.session.add(user)
        self.session.commit()

        result = self.session.query(domain.User).one()

        self.assertEqual(result.first_name, user.first_name)
        self.assertEqual(result.last_name, user.last_name)
        self.assertEqual(result.addresses[0].email, address.email)
        self.assertEqual(user.addresses[0].user, user)
