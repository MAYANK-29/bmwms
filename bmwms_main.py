# Main Python file 
#version 1.0 Alpha
#Author: Mithun
#Client: BMWMS
#Description:
#

from flask import Flask, render_template , request
import couchdb

user = "batman"
password = "iambatman"
couchserver = couchdb.Server("http://%s:%s@127.0.0.1:5984/" % (user, password))

current_db = couchserver["clustech"]

current_document = current_db["router_master"]

ulist = list(current_document["users"])

username = ulist[0]["username"]
dbname = ulist[0]["database"]
current_db = couchserver[dbname]
current_document = list(current_db["user_master"]["users"])
print(list(current_document))

################################################[APP LOGIC]###################################################################
app = Flask(__name__,template_folder="html/clustech/")

@app.route("/",methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		print(request.form["username"])
		print(request.form["password"])
		for item in current_document:
			if item.get('emp_username') == request.form["username"] and item.get('emp_password') == request.form["password"]:
				print("Found")
		return render_template("login.html")
	else:
		return render_template("login.html")

if __name__ == "__main__":
	app.run(debug=True)
################################################[APP LOGIC]###################################################################