"""
Routes and views for the flask application.
"""

from ast import Import
from datetime import datetime
from flask import redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'

db= SQLAlchemy(app)
#db1= SQLAlchemy(app)


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    about = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    
    def __repr__(self):
        return self.name
    
class PreGames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    version = db.Column(db.Float(), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    
    def __repr__(self):
        return self.name

with app.app_context():
    db.create_all()
    #db1.create_all()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='You wanna talk???'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='What is Ayu/Soft games?',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/library')
def library():
    games = Games.query.all()
    return render_template('library.html', title='Games Library', games=games)

@app.route('/server')
def discord():
    return render_template('discord_invite.html', title='JOIN!')

@app.route('/jdbrbhgbfnejbfjdbhsdbfh', methods=["POST","GET"])
def addgames():
    if request.method == "POST":
        g_name = request.form["gname"]
        about = request.form["about"]
        link = request.form["link"]
        new_game = Games(name = g_name,about = about,link = link)
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for("library"))
    else:
        return render_template('form.html', title='nigga')
@app.route('/jkdsjfknewkhnfannlknfn', methods=["POST","GET"])
def addunfinishedgames():
    if request.method == "POST":
        g_name = request.form["gname"]
        version = request.form["version"]
        link = request.form["link"]
        new_game = PreGames(name = g_name,version = version,link = link)
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for("library"))
    else:
        return render_template('form1.html', title='nigga')
@app.route("/prerelease")
def prerelease():
    pregames = PreGames.query.all()
    return render_template('prereleases.html', title="Pre Release", games=pregames)
@app.route("/library/<int:game_id>")
def game_page(game_id):
    game = Games.query.filter_by(id=game_id).first()
    return render_template('game.html', game=game)

@app.route("/bgjdwgfewfbhjcgbvdjsfwbhbhewjfbnewfcbw", methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        gname = request.form['gname']
        gtbr = Games.query.filter_by(name=gname).first()
        db.session.delete(gtbr)
        db.session.commit()
        return redirect(url_for("library"))
    return render_template('delete.html', title="delete")

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)