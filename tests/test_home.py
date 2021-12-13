def test_home(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "hello_santa": "Y",
        "environment": "dev",
        "testing": True,
    }