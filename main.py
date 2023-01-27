from flask import Flask,Blueprint,request,Response

app = Flask(__name__)

blueprint = Blueprint('sample', __name__)

# PROCESS QUESTION ANSWER MODEL OUTPUTS
@blueprint.route('/', methods=["POST"])
def handle():
    print(request.data)
    return Response(status=200)


app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run()