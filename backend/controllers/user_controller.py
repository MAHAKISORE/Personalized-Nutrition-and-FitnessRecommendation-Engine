from backend.domain.repositories.user_repository import UserRepositoryInterface
from flask import *
from backend.view.config import AppConfig
from backend.domain.usecase.signIn_usecase import SignInUsecase
from backend.domain.usecase.updateHealth_usecase import UpdateHealthUsecase
from backend.domain.usecase.login_usecase import LoginUsecase
from backend.domain.usecase.updateFood_usecase import UpdateFoodUsecase


class UserController:
    @staticmethod
    def create_routes(app:Flask,upi:UserRepositoryInterface):
        @app.route(AppConfig.signIn_url,methods=['GET','POST'])
        def page():
            signIn_usecase = SignInUsecase(user_repo=upi)
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
            login_usecase = LoginUsecase(upi=upi)
            # auth = UserAuth()
            if(request.method== "POST"):
                body = request.get_json()
                res =login_usecase.login(body)
                return res
            if(request.method == "GET"):
                return "hello world"   
    

        @app.route(AppConfig.health_update_url,methods=['POST'])
        def health_update():
            body = request.get_json()
            updateHealth_usecase = UpdateHealthUsecase(upi=upi)
            res = updateHealth_usecase.updateHealthModel(json_data=body)
            return res
        @app.route(AppConfig.food_update_url,methods = ["POST"])
        def food_update():
            body = request.get_json()
            updateFood_usecase = UpdateFoodUsecase(user_repo=upi)
            # food_controller = FoodController()
            res = updateFood_usecase.updateFood(json_data=body)
            return res