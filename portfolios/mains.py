from flask import Flask, render_template

App = Flask(__name__)

@App.route('/')
def base():
    return render_template("base.html")

@App.route('/home')
def home():
    return render_template("home.html")

@App.route('/about')
def about():
    return render_template("about.html")

@App.route('/product')
def product():
    return render_template("product.html")

@App.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    App.run(debug=True)