from flask import Flask, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['codes']

@app.route('/code', methods=['GET'])
def get_code():
    latest_code = collection.find_one(sort=[("date", pymongo.DESCENDING)])
    return jsonify({'code': latest_code['code']})

if __name__ == '__main__':
    app.run()