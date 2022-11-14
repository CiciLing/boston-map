from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

username = 'Cici'

# import map to the layout
# button: start drawing
# display a locations pop ups

@app.route('/')
def web_layout():
    return render_template('layout.html', username=username)

@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)