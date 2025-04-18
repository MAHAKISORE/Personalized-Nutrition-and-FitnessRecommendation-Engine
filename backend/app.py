from flask import Flask,render_template,request
from repository.user_auth import UserAuth
from database.food import Foods

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("main.html")


@app.route("/signIn",methods=['GET','POST'])

def page():
    auth = UserAuth()
    if(request.method == "GET"):
      
        return render_template("register.html")
    if(request.method == "POST"):
        body = request.get_json()
        res = auth.signIn(body)
        return res
    return

@app.route("/login",methods=['GET','POST'])
def login():
    auth = UserAuth()
    if(request.method== "POST"):
        body = request.get_json()
        res =auth.login(body)
        return res
    if(request.method == "GET"):
        return "hello world"


@app.route('/search',methods=['GET'])
def search():
    name = request.args.get('name')
    sorted_list = Foods().search_data(name)
    return sorted_list

app.run(debug=True)
print("hello")