from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint."""
    return jsonify({"message": "Personal Blog API"})

if __name__ == '__main__':
    app.run(debug=True)
