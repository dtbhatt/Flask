from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    image = "/static/tmnt.png"
    return render_template('ninja.html', image=image)

@app.route('/ninjas/<ninjacolor>')
def ninjaspurple(ninjacolor):
    if ninjacolor == "blue":
        image = "/static/leonardo.jpg"
    elif ninjacolor == "orange":
        image = "/static/michelangelo.jpg"
    elif ninjacolor == "red":
        image = "/static/raphael.jpg"
    elif ninjacolor == "purple":
        image = "/static/donatello.jpg"
    else:
        image = "/static/notapril.jpg"
    return render_template('ninja.html', image=image)




app.run(debug=True)




