from flask import Flask,jsonify
from werkzeug.wrappers import request

app=Flask(__name__)

tasks=[
    {
        "id":1,
        "task":"attend classes as well as coding classes",
        "done":False
    },
    {
         "id":2,
        "task":"have dinner",
        "done":False
    }
]

@app.route("/")
def printName():
    return ('rohini!')


@app.route("/getdata")
def getdata():
    return jsonify({
        "data":tasks
    })

@app.route("/adddata",methods=["POST"])
def adddata():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"plse provide the data"
        },400)
    task={
         "id":3,
        "task":request.json["task"],
        "done":False
    }
    tasks.append(task)
    return jsonify({
         "status":"success",
            "message":"task added successfully"
    })    

if __name__=="__main__":
    app.run(debug=True)


