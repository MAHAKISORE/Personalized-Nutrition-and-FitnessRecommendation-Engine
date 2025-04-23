from flask import Flask,render_template,request,make_response
from .controller.user_auth import UserAuth
from .controller.health_controller import HealthController
from .data_layer.repository.food_repository import FoodRepository
from flask_cors import CORS
from .view.config import AppConfig
from.controller.food_controller import FoodController
import json

#Creating Flask instance
app = Flask(__name__)
food_controller = FoodController()

#Cross Origin Resource Sharing
CORS(app)

#Configuring the app routes
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
    # sorted_list = FoodRepository().searchFood(name)
    sorted_list = food_controller.searchFood(query=name)
    return sorted_list

@app.route(AppConfig.health_update_url,methods=['POST'])
def health_update():
    body = request.get_json()
    res = HealthController().updateHealthModel(body)
    return res

@app.route(AppConfig.food_update_url,methods = ["POST"])
def food_update():
    body = request.get_json()
    # food_controller = FoodController()
    res = food_controller.updateFood(json_data=body)

    return res
@app.route(AppConfig.high_protein_diet,methods = ["POST"])
def get_high_protein_diet():
    body = request.get_json()
    calorie = request.args.get("calorie")
    print(calorie)
    # food_controller = FoodController()
    return food_controller.high_protein_diet(json_data=body,calorie=float(calorie))

@app.route("/user/update/<id>",methods=["POST"])
def updateUser(id):
    body = request.get_json()
    return food_controller.update(id=id,json_data=body)
    
@app.route(AppConfig.high_protein_diet+"/<id>",methods = ["POST"])
def get_diet(id):
  
    return food_controller.get_diet(id=id)
#running the app
app.run(debug=True)
