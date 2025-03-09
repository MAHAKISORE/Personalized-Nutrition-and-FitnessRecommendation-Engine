from flask import Flask,render_template,request
from .controller.user_auth import UserAuth
from .controller.health_controller import HealthController
from .data_layer.repository.food import Foods

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("signIn_login/main.html")


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

@app.route('/user/healthUpdate',methods=['POST'])
def update():
    body = request.get_json()
    res = HealthController().updateHealthModel(body)
    return res
    
    

app.run(debug=True)
print("hello")