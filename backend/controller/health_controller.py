from ..data_layer.repository.health import HealthDataProvider
from ..data_layer.repository.user import UserRepository

class HealthController(UserRepository):
    def __init__(self):
        pass

    def updateHealthModel(self,json_data):
            # print(json_data["id"])
            health_data = HealthDataProvider(id=json_data["id"])
            health_data.updateHeathFields(json_data=json_data)
            return "Updated!"