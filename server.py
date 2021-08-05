from flask import Flask, jsonify, request, render_template
from database import initialize, insert


#initialize database 
initialize.init()


# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)


#Routes 

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/read")
def read():
    #read database
	#jsonify data
	#return data
	return "no test data yet"
		

@app.route('/login', methods=['GET', 'POST'])
def login():
	# add database call to test 
	insert.insert("basil", 1,2,3)
	print("POST request")
	return "Hello World!"



# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
	# Runs the Flask application only if the main.py file is being run.
	app.run()