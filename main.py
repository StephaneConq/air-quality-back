from flask import Flask, request, jsonify
import json

from flask_cors import CORS

from src.airqualityController import AirQualityController
from src.polygonController import PolygonController

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/sync_polygons')
def sync_polygons():
    polygon_controller = PolygonController()
    polygon_controller.sync_polygons()
    return jsonify({})


@app.route('/api/polygon')
def get_polygon():
    polygon_controller = PolygonController()
    polygon = polygon_controller.get_city(request.args.get('city'))
    return jsonify({'polygon': polygon})


@app.route('/api/cities')
def get_cities():
    polygon_controller = PolygonController()
    cities = polygon_controller.get_all_cities()
    return jsonify(cities)


@app.route('/api/air_quality')
def get_air_quality():
    airquality_controller = AirQualityController()
    if request.args.get('lat') and request.args.get('lng'):
        return airquality_controller.get_by_coordinates(request.args.get('lat'), request.args.get('lng'))
    if request.args.get('city') and request.args.get('state') and request.args.get('country'):
        return airquality_controller.get_by_city(request.args.get('city'),
                                                 request.args.get('state'),
                                                 request.args.get('country'))
    return jsonify({})


if __name__ == '__main__':
    app.run()
