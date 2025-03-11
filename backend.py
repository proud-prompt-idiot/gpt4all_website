from gpt4all import GPT4All
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os



model_path = r"C:\Users\phwec\OneDrive\Code\line_detection\chatgpt_code\gpt4all_website\gpt4all-falcon-newbpe-q4_0.gguf" 
gpt_model = GPT4All(model_path)

app = Flask(__name__, static_folder="static")  # Serve static files from "static" folder
CORS(app)

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    print(user_input)

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = gpt_model.generate(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)