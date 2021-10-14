import json
import flask
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'something_special'


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions

@app.route('/')
def index(error=None):
    return render_template('index.html', error=error)


competitions = loadCompetitions()
clubs = loadClubs()
actual_club = None


@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        alone_club = [club for club in clubs if club["email"] == request.form["email"]][0]
    except IndexError:
        return index("Sorry, that email was not found.")
    for club in clubs:
        for competition in competitions:
            club[competition["name"]] = False

    for competition in competitions:
        date_compet = datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
        if date_compet < datetime.now():
            competition["past"] = True
        else:
            competition["past"] = False
    global actual_club
    actual_club = alone_club
    alone_club['points'] = int(alone_club['points'])
    return render_template('welcome.html',club=alone_club,competitions=competitions,clubs = clubs)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
    except:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=actual_club, competitions=competitions, clubs=clubs)

    if foundClub and foundCompetition:
        foundClub['points'] = int(foundClub['points'])
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=actual_club, competitions=competitions,clubs = clubs)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    club[competition['name']] = True
    placesRequired = int(request.form['places'])

    if placesRequired > club['points']:
        flash("Trop de points attribués")
        return render_template('welcome.html', club=actual_club, competitions=competitions,clubs = clubs)
    if placesRequired % 3 != 0:
        flash("Il faut 3 points pour réserver une place")
        return render_template('welcome.html', club=actual_club, competitions=competitions,clubs = clubs)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])- int((placesRequired/3))
    club['points'] = int(club['points']) - placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=actual_club, competitions=competitions,clubs = clubs)



@app.route('/display')
def show_clubs():
    return render_template('display.html',clubs = clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))