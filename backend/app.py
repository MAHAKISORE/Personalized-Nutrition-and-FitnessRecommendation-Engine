from flask import Flask,render_template,request,make_response
from .domain.usecase.updateHealth_usecase import UpdateHealthUsecase
from .data.data_sources.food_datasource import FoodDatasource
from flask_cors import CORS
from .view.config import AppConfig

from backend.data.repositories.food_repository import FoodRepository
from .domain.usecase.signIn_usecase import SignInUsecase
from .domain.usecase.login_usecase import LoginUsecase
from .domain.usecase.updateFood_usecase import UpdateFoodUsecase
from .domain.usecase.searchFood_usecase import SearchFoodUsecase
from backend.data.repositories.user_repository import UserRepository

#Creating Flask instance
app = Flask(__name__)
food_repo = FoodRepository()
user_repo = UserRepository()

#Cross Origin Resource Sharing
CORS(app)

#Configuring the app routes
@app.route(AppConfig.start_url)
def hello_world():
    return {"name":"hello there!"}
    

@app.route(AppConfig.signIn_url,methods=['GET','POST'])
def page():
    signIn_usecase = SignInUsecase(user_repo=user_repo)
    # auth = UserAuth()
    if(request.method == "GET"):
        return render_template("register.html")
    if(request.method == "POST"):
        body = request.get_json()   
        res = signIn_usecase.signIn(body)
        response = make_response(res)
        return response
    

@app.route(AppConfig.login_url,methods=['GET','POST'])
def login():
    login_usecase = LoginUsecase(user_repo)
    # auth = UserAuth()
    if(request.method== "POST"):
        body = request.get_json()
        res =login_usecase.login(body)
        return res
    if(request.method == "GET"):
        return "hello world"


@app.route(AppConfig.search_url,methods=['GET'])
def search():
    name = request.args.get('name')
    search_usecase = SearchFoodUsecase(upi=food_repo)
    # sorted_list = FoodRepository().searchFood(name)
    sorted_list = search_usecase.searchFood(query=name)
    return sorted_list

@app.route(AppConfig.health_update_url,methods=['POST'])
def health_update():
    body = request.get_json()
    updateHealth_usecase = UpdateHealthUsecase(upi=user_repo)
    res = updateHealth_usecase.updateHealthModel(json_data=body)
    return res

@app.route(AppConfig.food_update_url,methods = ["POST"])
def food_update():
    body = request.get_json()
    updateFood_usecase = UpdateFoodUsecase(user_repo=user_repo)
    # food_controller = FoodController()
    res = updateFood_usecase.updateFood(json_data=body)
    return res
    
#running the app
app.run(debug=True)
