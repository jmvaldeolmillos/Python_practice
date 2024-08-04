from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/hello')
def hello() -> str:
    return "Hello World!"


@app.route('/greet/<name>')
def greet(name: str) -> str:
    return f"Hello, {name}!"


@app.route('/add/<int:num1>/<int:num2>')
def add(num1: int, num2: int) -> str:
    return f"{num1} + {num2} = {num1 + num2}"


# manejo de parametros en Flask
# http://192.168.1.34:5555/handle_url_params?name=Jose&age=54
@app.route('/handle_url_params')
def handle_params() -> str:
    if 'name' in request.args.keys() and 'age' in request.args.keys():
        # return str(request.args)
        name = request.args.get('name')
        age = request.args.get('age')
        return f"Hello!! Your name: {name} and your age: {age}"
    else:
        return "No name or age found in params"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
