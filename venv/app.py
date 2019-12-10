from flask import Flask, render_template
from co2globalem import Co2globalem
from glaciers import Glaciers
from globaltemp import Globaltemp
from carbon import Carbon
from elec import Elec

app = Flask(__name__)

Co2globalem = Co2globalem()
Glaciers = Glaciers()
Globaltemp = Globaltemp()
Carbon = Carbon()
Elec = Elec()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/co2globalem')
def co2globalem():
    return render_template('co2globalem.html', co2globalem=Co2globalem)

@app.route('/glaciers')
def glaciers():
    return render_template('glaciers.html', glaciers=Glaciers)


@app.route('/globaltemp')
def globaltemp():
    return render_template('globaltemp.html', globaltemp=Globaltemp)

@app.route('/carbon')
def carbon():
    return render_template('carbon.html', carbon=Carbon)

@app.route('/elec')
def elec():
    return render_template('elec.html', elec=Elec)

if __name__ == '__main__':
    app.run(debug=True)
