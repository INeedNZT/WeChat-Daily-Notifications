from time import sleep
from collector import WeatherCollector as w, EndearmentCollector as e, DailyEngCollector as d, JokeCollector as j, ConstCollector as c
from datetime import datetime, date, timedelta


class Builder():
    def __init__(self):
        pass

    def _getWeather(self):
        r = w().getWeatherByLoc(31, 120)
        weather = r.get('weather')[0]
        desc = weather.get('description')
        main = r.get('main')
        temp = round(main.get('temp'))
        feel = round(main.get('feels_like'))

        return {'desc': desc, 'temp': str(temp) + "℃", 'feel': str(feel) + "℃"}
    
    def _getConst(self):
        r = c('sagittarius').getConst()
        d = {'index': '', 'sug': ''}
        for x in r:
            type = x.get('type')
            content = x.get('content')
            if type == '综合指数':
                d['index'] = content
            if type == '幸运数字':
                d['num'] = content
            if type == '幸运颜色':
                d['color'] = content
            if type == '今日概述':
                d['sug'] = content
        
        return d

    def build(self):
        w = self._getWeather()
        c = self._getConst() 

        de = d().getDailyEng()
        jk = j().getJoke()

        while (len(de)) > 68:
            sleep(2)
            print('Recall Daily English API for over length...')
            de = d().getDailyEng()

            print ("Find appropriate length of English: " + str(len(de)))

        while (len(jk)) > 85:
            sleep(2)
            print('Recall Joke API for over length...')
            jk = j().getJoke()
        
            print ("Find appropriate length of joke: " + str(len(jk)))

        jsonObj = {
            'desc': {
                'value': w.get('desc'),
                'color': '#006633'
            },
            'temp': {
                'value': w.get('temp'),
                'color': '#0099FF'
            },
            'feel': {
                'value': w.get('feel'),
                'color': '#99CC33'
            },
            'endearment': {
                'value': e().getEndearment(),
                'color': '#FF66FF'
            },
            'dailyEng': {
                'value': de,
                'color': '#00CCFF'
            },
            'joke': {
                'value': jk,
                'color': '#999999'
            },
            'constIndex': {
                'value': c.get('index'),
                'color': '#993333'
            },
            'constNum': {
                'value': c.get('num'),
                'color': '#669933'
            },
            'constColor': {
                'value': c.get('color'),
                'color': '#6699CC'
            },
            'constSug': {
                'value': c.get('sug'),
                'color': '#999999'
            },
            'encounterDays': {
                'value': calcEncounterDays(),
                'color': '#FF9966'
            },
            'meetDays': {
                'value': calcMeetDays(),
                'color': '#E65D36'
            },
            'togDays': {
                'value': calcTogDays(),
                'color': '#FFCC66'
            },
            'weekDay': {
                'value': getWeekDay(),
                'color': '#CC3333'
            },
            'emoji1':{
                'value': '🌚'
            },
            'emoji2':{
                'value': '🌈'
            },
            'emoji3':{
                'value': '🤡'
            },
            'emoji4':{
                'value': '🔮'
            }
        }

        return jsonObj


def calcEncounterDays():
    start = datetime(2021, 7, 10)
    now = datetime.combine(date.today(), datetime.min.time())
    # add 1 day for timezone reason
    return (now - start).days + 1


def calcMeetDays():
    expected = datetime(2023, 6, 26)
    now = datetime.combine(date.today(), datetime.min.time())
    return (expected - now).days


def calcTogDays():
    separate = datetime(2022, 8, 10) - datetime(2022, 6, 5)
    return calcEncounterDays() - (separate.days)


def getWeekDay():
    cnWeekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
    # add 1 day for timezone reason
    today = date.today().__add__(timedelta(days=1))
    weekday = cnWeekdays[today.weekday()]

    return "{}, {}".format(today.strftime("%Y-%-m-%-d"), weekday)
