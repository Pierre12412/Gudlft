from server import app


def test_book_too_much():
    app.test_client().get('/')
    app.test_client().post('/showSummary', data=dict(email="admin@irontemple.com", ))
    app.test_client().get('/book/Fall%20Classic/Iron%20Temple')
    response = app.test_client().post('/purchasePlaces',
                                      data=dict(places=50, competition='Fall Classic', club='Iron Temple'))
    assert "Trop de points" in str(response.data)
    assert "Points available: 4" in str(response.data)


def test_book_not_multiple_3():
    app.test_client().get('/')
    app.test_client().post('/showSummary', data=dict(email="admin@irontemple.com", ))
    app.test_client().get('/book/Fall%20Classic/Iron%20Temple')
    response = app.test_client().post('/purchasePlaces',
                                      data=dict(places=4, competition='Fall Classic', club='Iron Temple'))
    assert "Il faut 3 points" in str(response.data)
    assert "Points available: 4" in str(response.data)


def test_book_places_allowed():
    app.test_client().get('/')
    app.test_client().post('/showSummary', data=dict(email="admin@irontemple.com", ))
    app.test_client().get('/book/Fall%20Classic/Iron%20Temple')
    response = app.test_client().post('/purchasePlaces', data=dict(places=3, competition='Fall Classic', club='Iron Temple'))
    assert "Points available: 1" in str(response.data)
