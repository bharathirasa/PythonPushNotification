import requests
import json

API_ACCESS_KEY='YOUR_API_ACCESS_KEY'

registrationIds=['DEVICE_REGISTRATION_ID']

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