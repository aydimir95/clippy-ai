from flask import Flask, request, jsonify, make_response
import json
from chatgpt import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({"message": "Please use Post"})

@app.route('/', methods=['POST'])
def send_msg():
    usermsg = request.get_json()
    print(usermsg)
    airesponse = callToOpenAI(usermsg['client'])
    print(airesponse)
    
    # Ensure the response is properly formatted as JSON
    response_data = {"response": airesponse}
    return jsonify(response_data)

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed"}), 405

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)