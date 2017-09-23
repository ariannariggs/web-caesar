from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

from caesar import rotate_string

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method= "POST">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0" />
        <textarea name="text">{0}</textarea>
        <input type="submit" name="submit"/>

    </body>
    </form>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return form.format(' ')

@app.route("/", methods=["POST"])
def encrypt():
    rotate = request.form['rot']
    rot = int(rotate)
    text = request.form['text']
    final_text = rotate_string(text, rot)
    return '<h1>'+ form.format(final_text) + '</h1>'

app.run()