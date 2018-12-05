from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    print("BooYa x 3!!")

def hello():
    print("hello yo")

def totes():
    print("this is totes.")

hello_world()
hello()
totes()
hello_world()
hello()
totes()
hello_world()
hello()
totes()
hello_world()
hello()
totes()
hello_world()
hello()
totes()
hello_world()
hello()
totes()
hello_world()
hello()
totes()
hello_world()
hello()
totes()

if __name__ == "__main__":
    application.run()
