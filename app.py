from flask import Flask,render_template,request
from repository.user_auth import UserAuth

from database.user import User
from Models.user_model import UserModel

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("Project.html")


@app.route("/signIn",methods=['GET','POST'])

def page():
    auth = UserAuth()
    if(request.method == "GET"):
        print(request.data)
        auth.signIn()
        return "hello world"
    if(request.method == "POST"):
        body = request.get_json()
        res = auth.signIn(body)
        return res


app.run(debug=True)

print("hello")