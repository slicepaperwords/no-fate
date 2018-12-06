from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    return("No Fate!!!!!")
    return("and stuff")

if __name__ == "__main__":
    application.run()
