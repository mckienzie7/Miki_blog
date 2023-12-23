from flask import Flask
from markupsafe import escape


app = Flask(__name__)

ret = 'mama'

@app.route("/home/<name>", strict_slashes=False)
def Hbnb(name):
    return name


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
