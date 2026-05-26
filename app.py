from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello! My web app is running in the cloud 🚀</h1>"

@app.route("/info")
def info():
    return "<p>This is a PaaS deployment via Render.com</p>"

if __name__ == "__main__":
    app.run()