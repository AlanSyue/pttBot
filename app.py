import sys
from PTTLibrary import PTT
import requests

def lineNotify(msg):
	token='{LINE Notify Token}' 
	url = "https://notify-api.line.me/api/notify"
	headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
	payload = {'message': msg}
	r = requests.post(url, headers = headers, params = payload)
	return r.status_code

ID = '{PTT ID}'
Password = '{PTT Password}'

PTTBot = PTT.Library()
try:
    PTTBot.login(ID, Password)
except PTT.Exceptions.LoginError:
    PTTBot.log('Login fail')
    sys.exit()
except PTT.Exceptions.WrongIDorPassword:
    PTTBot.log('Wrong ID or password')
    sys.exit()
except PTT.Exceptions.LoginTooOften:
    PTTBot.log('Login too often')
    sys.exit()
PTTBot.log('success')

HowManyNewMail = PTTBot.hasNewMail()
if HowManyNewMail > 0:
	lineNotify(f'You got {HowManyNewMail} mail(s)')
else:
    print('No new mail')

PTTBot.logout()