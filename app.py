from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return "<h1>Bienvenue sur mon application Flask !</h1><p>Allez à <a href='/about'>À propos</a></p>"

# Page "À propos"
@app.route('/about')
def about():
    return "<h1>À propos</h1><p>Ceci est une application web créée avec Flask.</p>"

def hhh():
    return "hhhhh"




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
