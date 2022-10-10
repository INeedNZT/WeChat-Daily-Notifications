# WeChat-Daily-Notifications


## Introduction
A small program of message push for Wechat Subscription. Made for my girlfriend lyw.

### Create Virtual Environment
python3 -m venv lib

source ./lib/bin/activate

deactivate (quit the virtual environment)

### Install Dependence
pip install -r requirements.txt

### Run Prog
python3 wxPush.py

### Unit Test
python3 unitTest

### Run Prog on Linux with background mode
nohup python3 -u wxPush.py > wxPush.log 2>&1 &

### check the pid for the running prog
ps aux | grep 'wxPush.py' | grep -v grep

### shut down the prog
kill pid