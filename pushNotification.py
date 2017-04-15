import requests
import json

API_ACCESS_KEY='AIzaSyAavPj-wjgeAGBl6QTcJyremlCTeEtxG0c'

registrationIds=['cV0Z7xnjG4g:APA91bEZhqZyPNjIK_xtb-3d169pHYfdIGgoTxAyC7F34pkWkoe4RSTZqY07PAMmJbL6ZhalFrFZOjSSQPV7-0o1iZsKA5mEio2ptEmomnmjUJ33mtseg2yYBOtNA-JsKeovwfHugLn6']

url = 'https://android.googleapis.com/gcm/send'

msg={'message':'here is a message. message',
	'title':'This is a title. title',
	'subtitle':'This is a subtitle. subtitle',
	'tickerText':'Ticker text here...Ticker text here...Ticker text here',
	'vibrate'	: 1,
	'sound'		: 1,
	'largeIcon'	: 'large_icon',
	'smallIcon'	: 'small_icon'
}
fields = {
	'registration_ids': registrationIds,
	'data': msg
}

# Adding empty header as parameters are being sent in payload
headers = {'Authorization':'key='+API_ACCESS_KEY,
	'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(fields), headers=headers)
print(r.content)