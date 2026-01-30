from flask import Flask, jsonify

app = Flask(__name__)

# "Home" route
@app.route('/')
def home():
    return "ATS Resume Reviewer - Active"

# "Health Check" route
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'module': 'ingestion'})

if __name__ == '__main__':
    app.run(debug=True)