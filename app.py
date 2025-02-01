from flask import Flask,render_template,request


from database.user import User
from Models.user_model import UserModel

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("Project.html")


@app.route("/signIn",methods=['GET','POST'])

def page():
    user = User()
    if(request.method == "GET"):
        print(request.data)
        user.signIn()
        return "hello world"
    if(request.method == "POST"):
        body = request.get_json()
        user.signIn(body)
        return "Hi there POST!"


app.run(debug=True)

print("hello")