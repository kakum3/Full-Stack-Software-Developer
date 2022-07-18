from flask import Flask,jsonify,request,json


app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
@app.route("/todos", methods=["GET"])

def hello_world():

    json_text = jsonify(todos)

    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request.get_json(force=True)
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    var=jsonify(todos)
    
    return var

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    something=jsonify(todos)
    return something

   
   


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)