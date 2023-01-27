from flask import Flask,Blueprint,request

app = Flask(__name__)

blueprint = Blueprint('sample', __name__)

@blueprint.route('/', methods=["POST"])
def post():
    print(request.data)
    return {}, 200


@blueprint.route('/', methods=["GET"])
def get():
    print(request.data)
    return "ping", 200


app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080")