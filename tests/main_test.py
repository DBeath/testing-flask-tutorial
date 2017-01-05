
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_not_found(client):
    response = client.get('/notfound')
    assert response.status_code == 404
