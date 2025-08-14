from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
	return jsonify({"message": "Todo chido"})
if __name__ == "__main__":
	app.run(threaded=True, host='0.0.0.0', port=3000)
