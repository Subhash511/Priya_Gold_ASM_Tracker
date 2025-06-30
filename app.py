from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def receive_stock():
    data = request.json
    print("Received stock data:", data)
    # url = 'https://script.google.com/macros/s/AKfycbySgYgzw2dA6vQunf0w3u75yTyl4Zt-XRksPedaYCiNW8lEDzeJFNj03VGAaE_tVmu3/exec'
    # response = requests.post(url, json=data)

    # # Print response
    # print("Google Status Code:", response.status_code)
    # print("Google Response Text:", response.text)
    # # Save data in json file
    # with open("response.txt", "w", encoding="utf-8") as file:
    #     json.dump(data, file, indent=4)

    return jsonify({"message": "Data received!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)