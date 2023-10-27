
def test_foo(client):
    res = client.get('/')
    assert res.status_code == 200