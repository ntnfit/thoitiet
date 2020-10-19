import pyrebase
import pdb
config = {
"apiKey": "AIzaSyB7HXfaO209Y2TdIKDIEwlySDtzI53B4Uc",
  "authDomain": "esp8266-c9b40.firebaseapp.com",
  "databaseURL": "https://esp8266-c9b40.firebaseio.com",
  "projectId": "esp8266-c9b40",
  "storageBucket": "esp8266-c9b40.appspot.com",
  "messagingSenderId": "552566677008",
  "appId": "1:552566677008:web:4e203ea1fdb315bad7b495",
  "measurementId": "G-F0KPE70H3Y"

}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *
import json

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
	todo = db.child("DHT11/Humidity").get()
	to = todo.val()

	nd = db.child("DHT11/Temperature").get()
	k = nd.val()

	last_nd = next(reversed(k.keys()))
	last_value_nd = k[last_nd]

	last_key = next(reversed(to.keys()))
	last_value = to[last_key]
	data = {'nhiet_do':last_value_nd,'do_am':last_value }
	return json.dumps(data)
	

@app.route('/', methods=['GET'])
def basic():
	
			todo = db.child("DHT11/Humidity").get()
			to = todo.val()

			nd = db.child("DHT11/Temperature").get()
			k = nd.val()

			last_nd = next(reversed(k.keys()))
			last_value_nd = k[last_nd]

			last_key = next(reversed(to.keys()))
			last_value = to[last_key]
			return render_template('index.html', t=[last_value,last_value_nd])
		

if __name__ == '__main__':
	app.run(debug=True)


