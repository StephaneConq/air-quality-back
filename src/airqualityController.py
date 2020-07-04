import requests
from credentials import AIR_VISUAL_KEY


class AirQualityController:

    def __init__(self):
        pass

    def get_by_coordinates(self, lat, lng):
        res = requests.get('https://api.airvisual.com/v2/nearest_city?lat={}&lon={}&key={}'.format(lat,
                                                                                                   lng,
                                                                                                   AIR_VISUAL_KEY))
        return res.json()

    def get_by_city(self, city, state, country):
        res = requests.get('https://api.airvisual.com/v2/city?city={}&state={}&country={}&key={}'.format(city,
                                                                                                         state,
                                                                                                         country,
                                                                                                         AIR_VISUAL_KEY))
        return res.json()
