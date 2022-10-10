import unittest
import builder as b
import wxPush as wx
from collector import WeatherCollector as w, EndearmentCollector as e, DailyEngCollector as d, JokeCollector as j, ConstCollector as c


class Testing(unittest.TestCase):
    def test_weatherApi(self):
        r = w().getWeatherByLoc(31, 120)
        print(r)
        self.assertIsNotNone(r, "Can't get weather info, the result is None.")

    def test_endearmentApi(self):
        r = e().getEndearment()
        self.assertIsInstance(
            r, str, "Can't get endearment, the result is not string.")

    def test_dailyEngApi(self):
        r = d().getDailyEng()
        self.assertIsInstance(
            r, str, "Can't get dailyEng, the result is not dict.")

    def test_jokeApi(self):
        r = j().getJoke()
        self.assertIsInstance(
            r, str, "Can't get Joke, the result is not string.")
    
    def test_constApi(self):
        r = c('libra').getConst()
        self.assertIsInstance(
            r, list, "Can't get Constellation, the result is not list.")

    def test_encounterDays(self):
        r = b.calcEncounterDays()
        self.assertGreater(r, 0, "The days must greater than 0.")

    def test_meetDays(self):
        r = b.calcMeetDays()
        self.assertGreater(r, 0, "The days must greater than 0.")

    def test_togDays(self):
        r = b.calcTogDays()
        self.assertGreater(r, 0, "The days must greater than 0.")

    def test_weekday(self):
        r = b.getWeekDay()
        self.assertIsInstance(r, str, "The weekday must be a string.")

    def test_builder(self):
        r = b.Builder().build()
        self.assertIsInstance(r, dict, "The build result should be a json dict.")
    
    def test_accessToken(self):
        r = wx.getAccessToken()
        self.assertIsInstance(r, str, "The access token should be a string.")


if __name__ == '__main__':
    unittest.main()
