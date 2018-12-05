from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    print("BooYa x 3!!")

hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()

if __name__ == "__main__":
    application.run()
