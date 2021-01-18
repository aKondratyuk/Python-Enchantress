import unittest
from unittest.mock import patch, PropertyMock
from hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        # optional method, may be used to initialize hen_house instance
        self.hen_house = HenHouse(hen_count=10)

    def test_init_with_less_than_min(self):
        # initialize HenHouse with hens_count less than HenHouse.min_hens_accepted
        # make sure error is raised
        with self.assertRaises(ValueError):
            self.hen_house = HenHouse(hen_count=4)

    def test_season(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        with patch('datetime.datetime') as datetime_mock:
            # winter
            months = [1, 2, 12]
            for month in months:
                datetime_mock.today().month = month
                self.assertEqual(self.hen_house.season, 'winter')
            # spring
            months = [3, 4, 5]
            for month in months:
                datetime_mock.today().month = month
                self.assertEqual(self.hen_house.season, 'spring')
            # summer
            months = [6, 7, 8]
            for month in months:
                datetime_mock.today().month = month
                self.assertEqual(self.hen_house.season, 'summer')
            # autumn
            months = [9, 10, 11]
            for month in months:
                datetime_mock.today().month = month
                self.assertEqual(self.hen_house.season, 'autumn')

    def test_productivity_index(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        with patch('hen_class.HenHouse.season', new_callable=PropertyMock) as season_mock:
            season_mock.return_value = 'winter'
            self.assertEqual(self.hen_house._productivity_index(), 0.25)
            season_mock.return_value = 'spring'
            self.assertEqual(self.hen_house._productivity_index(), 0.75)
            season_mock.return_value = 'summer'
            self.assertEqual(self.hen_house._productivity_index(), 1)
            season_mock.return_value = 'autumn'
            self.assertEqual(self.hen_house._productivity_index(), 0.5)

    def test_productivity_index_incorrect_season(self):
        # mock the season method return with some incorrect season
        # make sure ErrorTimesOfYear is raised when _productivity_index called
        with patch('hen_class.HenHouse.season', new_callable=PropertyMock) as season_mock:
            season_mock.return_value = 'fall'
            self.assertRaises(ErrorTimesOfYear, lambda: self.hen_house._productivity_index())

    def test_get_eggs_daily_in_winter(self):
        # test get_eggs_daily function
        # _productivity_index method or season should be mocked
        with patch('hen_class.HenHouse._productivity_index', new_callable=PropertyMock) as prod_mock:
            prod_mock().return_value = 0.25
            self.assertEqual(self.hen_house.get_eggs_daily(16), 4)

    def test_get_max_count_for_soup(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        with patch('hen_class.HenHouse.season', new_callable=PropertyMock) as season_mock:
            season_mock.return_value = 'spring'
            self.assertEqual(self.hen_house.get_max_count_for_soup(3), 5)

    def test_get_max_count_for_soup_returns_zero(self):
        # call get_max_count_for_soup with expected_eggs number bigger than get_eggs_daily(self.hen_count)
        # zero should be returned.

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        with patch('hen_class.HenHouse.season', new_callable=PropertyMock) as season_mock:
            season_mock.return_value = 'winter'
            self.assertEqual(self.hen_house.get_max_count_for_soup(7), 0)

    def test_food_price(self):
        # mock requests.get and make the result has status_code attr 200 and text to some needed value
        # make sure food-price() return will be of int type
        with patch('requests.get', new_callable=PropertyMock) as request_mock:
            request_mock.return_value.status_code = 200
            self.assertTrue(self.hen_house.food_price())

    def test_food_price_connection_error(self):
        # mock requests.get and make the result has status_code attr not 200
        # check that ConnectionError is raised when food_price method called
        with patch('requests.get', new_callable=PropertyMock) as request_mock:
            request_mock.return_value.status_code = 404
            self.assertRaises(ConnectionError, lambda: self.hen_house.food_price())


if __name__ == '__main__':
    unittest.main()
