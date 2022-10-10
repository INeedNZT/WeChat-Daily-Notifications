import requests
import configparser

config = configparser.ConfigParser()
config.read_file(open('config.ini', 'r'))
weatherKey = config.get('openweathermap.api', 'key')
tianKey = config.get('tianapi.api', 'key')
yesapiKey = config.get('yesapi.api', 'key')


# call open weather map to get weather info
class WeatherCollector():
    def __init__(self):
        self.url = 'https://api.openweathermap.org/data/2.5/weather'
        self.key = weatherKey
        self.lang = 'zh_cn'
        self.units = 'metric'

    def getWeatherByLoc(self, lat, lon):
        r = requests.get(
            self.url, {'lat': lat, 'lon': lon, 'lang': self.lang, 'units': self.units, 'appid': self.key})
        r.raise_for_status()

        return r.json()


# call tianapi to get Endearment
class EndearmentCollector():
    def __init__(self):
        self.url = 'http://api.tianapi.com/saylove/index'
        self.key = tianKey

    def getEndearment(self):
        r = requests.get(self.url, {'key': self.key})
        r.raise_for_status()

        jr = r.json()
        code = jr.get('code')
        if code != 200:
            raise Exception("Endearment request error, please check the API")

        content = jr.get('newslist')[0]
        return content.get('content')


# call tianapi to get Daily English recommend
class DailyEngCollector():
    def __init__(self):
        self.url = 'http://api.tianapi.com/ensentence/index'
        self.key = tianKey

    def getDailyEng(self):
        r = requests.get(self.url, {'key': self.key})
        r.raise_for_status()

        jr = r.json()
        code = jr.get('code')
        if code != 200:
            raise Exception(
                "Daily English request error, please check the API")
        content = jr.get('newslist')[0]
        en = content.get('en')
        zh = content.get('zh')

        return en.rstrip() + '\n' + zh.rstrip()


# call tianapi to get Joke
class JokeCollector():
    def __init__(self):
        # self.url = 'http://api.tianapi.com/joke/index'
        self.url = 'http://hd215.api.yesapi.cn/api/App/Common_Joke/RandOne'
        self.key = yesapiKey
        self.num = 1


    def getJoke(self):
        r = requests.get(self.url, {'app_key': self.key, 'num': self.num})
        r.raise_for_status()

        jr = r.json()
        code = jr.get('ret')
        if code != 200:
            raise Exception(
                "Joke request error, please check the API")

        list = jr.get('data').get('joke')

        return list[0][0].replace('\r', '')


# call tianapi to get Daily Constellation prediction
class ConstCollector():
    def __init__(self, astro):
        self.url = 'http://api.tianapi.com/star/index'
        self.key = tianKey
        self.astro = astro

    def getConst(self):
        r = requests.get(self.url, {'key': self.key, 'astro': self.astro})
        r.raise_for_status()

        jr = r.json()
        code = jr.get('code')
        if code != 200:
            raise Exception(
                "Constellation request error, please check the API")

        return jr.get('newslist')
