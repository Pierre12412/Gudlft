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
