from flask import Flask, request, jsonify
import json


# Set up a local web server
app = Flask(__name__)
@app.route('/')
def createpage():
    return
if __name__=='__main__':
    app.run(host="localhost",port=8080)
    
# Create a txt file named as "storage.txt"
f = open('strange.txt','w+')


@app.route('/write',methods=['POST'])
def writeInfo():
    tmp = request.get_json()
    new_phrase = tmp['phrase']
    with open("storage.txt","w") as f:
        f.write(new_phrase)
        f.write("\n")
    return
 
    
@app.route('/read',methods=['GET'])
def readInfo():
    with open("storage.txt","r") as f:
        content = [line.rstrip('/n') for line in f]
        data = { }
        data['phrase'] = content
        return jsonify(data)

