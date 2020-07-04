import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account
cred = credentials.Certificate('credentials/firebase-service-account.json')
firebase_admin.initialize_app(cred)


class PolygonController:

    def __init__(self):
        self.db = firestore.client()

    def delete_collection(self, collection, batch_size):
        docs = collection.limit(batch_size).stream()
        deleted = 0

        for doc in docs:
            print(f'Deleting doc {doc.id} => {doc.to_dict()}')
            doc.reference.delete()
            deleted = deleted + 1

        if deleted >= batch_size:
            return self.delete_collection(collection, batch_size)

    def get_city(self, city_name):
        doc_ref = self.db.collection('polygons').document(city_name)
        if doc_ref:
            doc = doc_ref.get()
            doc_json = doc.to_dict()
            if not doc_json:
                return None
            doc_json['coordinates'] = json.loads(doc_json['polygons'])
            return doc_json
        return None

    @staticmethod
    def get_all_cities():
        cities = {}
        with open('geojson/cities.json') as city_json:
            cities = json.load(city_json)
        return cities
