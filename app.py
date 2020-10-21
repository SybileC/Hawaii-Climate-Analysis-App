from flask import Flask

# Create an app
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
if __name__ == "__main__":
    app.run(debug=True)
