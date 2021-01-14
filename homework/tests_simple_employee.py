import requests
import unittest
from unittest import mock


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


class TestEmployee(unittest.TestCase):
    def test_email(self):
        test_manager = Employee('andrii', 'kondratyuk', 2000)
        self.assertEqual(test_manager.email, 'andrii.kondratyuk@email.com')

        test_programmer = Employee('peter', 'pan', 800)
        self.assertEqual(test_programmer.email, 'peter.pan@email.com')

    def test_fullname(self):
        test_manager = Employee('andrii', 'kondratyuk', 2000)
        self.assertEqual(test_manager.fullname, 'andrii kondratyuk')

        test_programmer = Employee('peter', 'pan', 800)
        self.assertEqual(test_programmer.fullname, 'peter pan')

    def test_apply_raise(self):
        test_manager = Employee('andrii', 'kondratyuk', 2000)
        pay = test_manager.pay
        test_manager.apply_raise()
        self.assertEqual(test_manager.pay, int(pay*1.05))

        with self.assertRaises(TypeError):
            test_weird_manager = Employee('andrii', 'kondratyuk', '2000')
            test_weird_manager.apply_raise()

        test_programmer = Employee('peter', 'pan', 800)
        pay = test_programmer.pay
        test_programmer.apply_raise()
        self.assertEqual(test_programmer.pay, int(pay*1.05))

        with self.assertRaises(TypeError):
            test_weird_programmer = Employee('peter', 'pan', '800')
            test_weird_programmer.apply_raise()

    def mock_request(self):
        class Requests:
            def get(self, text):
                pass
            ok = True
        return Requests()

    @mock.patch('homework_3.tests_simple_employee.requests', side_effect=mock_request)
    def test_monthly_schedule(self, response):
        test_manager = Employee('andrii', 'kondratyuk', 2000)
        test_manager.monthly_schedule(6)
