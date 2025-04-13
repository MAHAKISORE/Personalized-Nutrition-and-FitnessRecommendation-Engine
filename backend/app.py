from flask import Flask
from flask_cors import CORS
from backend.controllers.user_controller import UserController
from backend.data.repositories.food_repository import FoodRepository
from backend.data.repositories.user_repository import UserRepository
from backend.controllers.food_controller import FoodController

#Creating Flask instance

class Nutrify:
    @staticmethod
    def run():
        app = Flask(__name__)
        food_repo = FoodRepository()
        user_repo = UserRepository()

        #Cross Origin Resource Sharing
        CORS(app)

        #Configuring the app routes
        UserController.create_routes(app=app,upi=user_repo)
        FoodController.create_routes(app=app,fpi=food_repo)

        app.run(debug=True)

Nutrify.run()