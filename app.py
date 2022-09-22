from itertools import product
from flask import Flask

student_id = 15
print(list(product(
    ('python 3.8.*', 'python 3.7.*', 'python 3.6.*'),
    ('venv + requirements.txt', 'virtualenv + requirements.txt', 'poetry', 'pipenv')
))[(student_id - 1) % 12])

app = Flask(__name__)

@app.route(f"/api/v1/hello-world-{student_id}")
def hello_world():
    return f"Hello World {student_id}"