import requests
import builder
import configparser
from apscheduler.schedulers.blocking import BlockingScheduler


# get config info
config = configparser.ConfigParser()
config.read_file(open('config.ini', 'r'))
PORT = config.getint('server', 'port')
appID = config.get('wx.api', 'appID')
appsecret = config.get('wx.api', 'appsecret')
users = config.get('wx.users', 'userIds').split(',')  # list
morningTemplate = config.get('wx.templates', 'morning')


def getAccessToken():
    payload = {'grant_type': 'client_credential',
               'appid': appID, 'secret': appsecret}
    r = requests.get('https://api.weixin.qq.com/cgi-bin/token',
                     params=payload)
    r.raise_for_status()
    content = r.json()
    return content.get('access_token')


def push(userId, templateId):
    token = {'access_token': getAccessToken()}
    data = builder.Builder().build()
    emphasis = 'togDays.DATA'
    body = {'touser': userId, 'template_id': templateId,
            'topcolor': '#FF0000', 'data': data, 'emphasis_keyword': emphasis}
    r = requests.post(
        'https://api.weixin.qq.com/cgi-bin/message/template/send', params=token, json=body)
    r.raise_for_status()

    content = r.json()
    if content.get('errcode') != 0:
        raise Exception("WX push failed, please check the API")
    

def job():
    print("job begin...")
    for user in users:
        push(user, morningTemplate)

if __name__ == '__main__':
    scheduler = BlockingScheduler({})
    scheduler.add_job(job, "cron", hour=16, minute=30)
    scheduler.start()
    # job()

# scheduler = BackgroundScheduler()
# scheduler.add_job(job, "cron", hour=5, minute=55)
# scheduler.start()

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<p>我爱lyw</p>"


# if __name__ == '__main__':
#     app.run('0.0.0.0', PORT)
