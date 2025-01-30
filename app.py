from flask import Flask,render_template,request
from database.user import User

app = Flask(__name__)




@app.route("/")
def hello_world():
    return render_template("Project.html")


@app.route("/signIn",methods=['GET'])

def page():
    user = User()
    if(request.method == "GET"):
        print(request.data)
        user.signIn()
        return "hello world"





app.run(debug=True)

print("hi")