from flask import Flask, request, jsonify
import json

#--------------Assumption-----------------
# I assume when I run for sending or 
# receiving a request to or from a server,
# there should be a qualified post body.
#-----------------------------------------

#-------------- Step One ------------------
# Set up a local web server
#-----------------------------------------
app = Flask(__name__)
@app.route('/')
def createpage():
    return
if __name__=='__main__':
    app.run(host="localhost",port=8080)
    
#-------------- Step Two -----------------
# Create a txt file named as "storage.txt"
#-----------------------------------------
f = open('strange.txt','w+')



#------------- Step Three ----------------
# Create a write endpoint will accept POST
# request and take a single JSON parameter,
# 'phrase' and write it at the end of the 
# file. The post body would be of the form:
#     {phrase: "<phrase>"}
#-----------------------------------------
@app.route('/write',methods=['POST'])
def writeInfo():
    tmp = request.get_json()
    new_phrase = tmp['phrase']
    with open("storage.txt","w") as f:
        f.write(new_phrase)
        f.write("\n")
    return
 

#------------- Step Three ----------------
# Create a read endpoint will accept GET
# request and return each phrase in the
# list as a single JSON object of the 
# form:
#     {phrase: ["<phrase1>",...,"<phrasen>"]}
#-----------------------------------------
@app.route('/read',methods=['GET'])
def readInfo():
    with open("storage.txt","r") as f:
        content = [line.rstrip('/n') for line in f]
        data = { }
        data['phrase'] = content
        return jsonify(data)

