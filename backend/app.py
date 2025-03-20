from flask import Flask,render_template,request,make_response
from .controller.user_auth import UserAuth
from .controller.health_controller import HealthController
from .data_layer.repository.food_repository import FoodRepository
from flask_cors import CORS
from .view.config import AppConfig
from.controller.food_controller import FoodController

app = Flask(__name__)
CORS(app)


@app.route(AppConfig.start_url)
def hello_world():
    return {"name":"hello there!"}


@app.route(AppConfig.signIn_url,methods=['GET','POST'])
def page():
    auth = UserAuth()
    if(request.method == "GET"):
        return render_template("register.html")
    if(request.method == "POST"):
        body = request.get_json()   
        res = auth.signIn(body)
        response = make_response(res)
        return response
    

@app.route(AppConfig.login_url,methods=['GET','POST'])
def login():
    auth = UserAuth()
    if(request.method== "POST"):
        body = request.get_json()
        res =auth.login(body)
        return res
    if(request.method == "GET"):
        return "hello world"


@app.route(AppConfig.search_url,methods=['GET'])
def search():
    name = request.args.get('name')
    sorted_list = FoodRepository().search_data(name)
    return sorted_list

@app.route(AppConfig.health_update_url,methods=['POST'])
def health_update():
    body = request.get_json()
    res = HealthController().updateHealthModel(body)
    return res

@app.route(AppConfig.food_update_url,methods = ["POST"])
def food_update():
    body = request.get_json()
    food_controller = FoodController()
    res = food_controller.updateFood(json_data=body)

    return res
    
    
app.run(debug=True)
