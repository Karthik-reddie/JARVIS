from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ JARVIS is running!"

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    message = data.get("message", "")
    response = f"JARVIS received: {message}"  # you can plug your logic here
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
