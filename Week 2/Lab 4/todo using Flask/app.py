from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
todos = []
next_id = 1


def find_todo(todo_id):
    return next((t for t in todos if t["id"] == todo_id), None)


# CREATE - Add a new todo
@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    data = request.get_json(silent=True) or {}

    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400

    todo = {
        "id": next_id,
        "title": title,
        "description": data.get("description", ""),
        "completed": data.get("completed", False),
    }
    todos.append(todo)
    next_id += 1

    return jsonify(todo), 201


# READ - Get all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200


# READ - Get a single todo by id
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = find_todo(todo_id)
    if not todo:
        return jsonify({"error": "todo not found"}), 404
    return jsonify(todo), 200


# UPDATE - Update an existing todo (full or partial)
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = find_todo(todo_id)
    if not todo:
        return jsonify({"error": "todo not found"}), 404

    data = request.get_json(silent=True) or {}

    todo["title"] = data.get("title", todo["title"])
    todo["description"] = data.get("description", todo["description"])
    todo["completed"] = data.get("completed", todo["completed"])

    return jsonify(todo), 200


# DELETE - Remove a todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = find_todo(todo_id)
    if not todo:
        return jsonify({"error": "todo not found"}), 404

    todos.remove(todo)
    return jsonify({"message": f"todo {todo_id} deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)