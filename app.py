from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory store
news = [
    {"id": 0, "title": "Hello", "content": "First news"}
]
next_id = 1  # auto-increment for IDs


# Home route
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Flask News API!"})


# 2.1 - GET /news (list all)
@app.route("/news", methods=["GET"])
def list_news():
    return jsonify({"count": len(news), "items": news})


# 2.2 - POST /news (create new)
@app.route("/news", methods=["POST"])
def create_news():
    global next_id
    data = request.json
    if not data or "title" not in data or "content" not in data:
        abort(400, description="Missing title or content")

    new_item = {
        "id": next_id,
        "title": data["title"],
        "content": data["content"]
    }
    news.append(new_item)
    next_id += 1
    return jsonify(new_item), 201


# GET /news/<id> (single item by id)
@app.route("/news/<int:item_id>", methods=["GET"])
def get_news(item_id):
    for item in news:
        if item["id"] == item_id:
            return jsonify(item)
    abort(404, description="News not found")


# 2.3 - PUT /news/<id> (update by id)
@app.route("/news/<int:item_id>", methods=["PUT"])
def update_news(item_id: int):
    for item in news:
        if item["id"] == item_id:
            data = request.json
            for key in ("title", "content"):
                if key in data:
                    item[key] = data[key]
            return jsonify(item)
    abort(404, description="News not found")


# 2.3 - DELETE /news/<id> (delete by id)
@app.route("/news/<int:item_id>", methods=["DELETE"])
def delete_news(item_id: int):
    for i, item in enumerate(news):
        if item["id"] == item_id:
            del news[i]
            return jsonify({"status": "deleted", "id": item_id})
    abort(404, description="News not found")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

