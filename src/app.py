#pipenv run python src/app.py

from flask import Flask, request, jsonify,json

app = Flask(__name__)

global todos
todos = [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])

def hello_world():

    #json_text = jsonify(todos)
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    print(todos)
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print(todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print(position)
    print(len(todos))
    if len(todos) == 0:
        msj = "La lista esta vacia no se puede elimar mas nada"
        return jsonify(msj)

    elif len(todos) >= position:
        todos.pop(position)
        msj = f"This is the position to delete:{position}, quedan en las lista: {todos}"
        print("This is the position to delete: ",position)
        return jsonify(todos)
    else:
        msj = " el valor a eliminar no existe intente nuevamente"
        return jsonify(msj)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)