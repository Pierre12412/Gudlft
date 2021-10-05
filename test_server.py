import pytest
from server import app


def test_connexion_wrong():
    response = app.test_client().post('/showSummary',data=dict(email='jean@jean.fr',))
    assert "Sorry, that email was not found." in str(response.data)
    assert response.status_code == 200


def test_connexion_right():
    response = app.test_client().post('/showSummary',data=dict(email="admin@irontemple.com",))
    assert not "Sorry, that email was not found." in str(response.data)
    assert response.status_code == 200
    assert 'Welcome, admin@irontemple.com' in str(response.data)

def test_finished_or_not():
    app.test_client().post('/showSummary',data=dict(email="admin@irontemple.com"))
    response = app.test_client().get('/showSummary')
    assert 'Competition is finished' or 'Hurry up' in str(response.data);

def test_show_clubs():
    response = app.test_client().post('/showSummary', data=dict(email="admin@irontemple.com"))
    assert 'Clubs:' in str(response.data)

def test_display():
    response = app.test_client().get('/display')
    assert 'Iron Temple' in str(response.data)