import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index(error=None):
    return render_template('index.html',error=error)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    multiple_club = [club for club in clubs if club['email'] == request.form['email']]
    for club in clubs:
        for competition in competitions:
            club[competition['name']] = False
    try:
        alone_club = multiple_club[0]
    except IndexError:
        return index("Sorry, that email was not found.")
    for competition in competitions:
        date_compet = datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S')
        actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        actual = datetime.strptime(actual, '%Y-%m-%d %H:%M:%S')
        if date_compet < actual:
            competition['past'] = True
        else:
            competition['past'] = False
    return render_template('welcome.html',club=alone_club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]

    if foundClub and foundCompetition:
        foundClub['points'] = int(foundClub['points'])
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    club[competition['name']] = True
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)



# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))