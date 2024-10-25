from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"  # This can be replaced with your actual content

if __name__ == '__main__':
    app.run(debug=True)