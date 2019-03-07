import pyrebase
from flask import Flask, render_template, request
app = Flask(__name__)



config = {
	"apiKey": "AIzaSyCbyFqESMXhsjc8IOroX6I8zY3WpimOnbw",
    "authDomain": "pythonbd-6c49a.firebaseapp.com",
    "databaseURL": "https://pythonbd-6c49a.firebaseio.com",
    "projectId": "pythonbd-6c49a",
    "storageBucket": "pythonbd-6c49a.appspot.com",
    "messagingSenderId": "976742913076"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()




@app.route('/', methods=['GET', 'POST'])

def basic():
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		user = auth.sign_in_with_email_and_password(email,password)
		auth.get_account_info(user['idToken'])
		return render_template('page.html')
	return render_template('new.html')




if __name__ == '__main__':
	app.run()
