from flask import session
import pytest
from types import SimpleNamespace
from flask_app.forms import CreatePostForm

def test_index_route_exists(client):
    res = client.get('/')
    assert res.status_code == 200

def test_logout_works(client, auth):
    auth.register()
    auth.login()

    with client:
        client.get('/')    
        assert session['_user_id'] == 'test'

    res = auth.logout()
    assert res.status_code == 302
    with client:
        client.get('/')
        assert '_user_id' not in session


@pytest.mark.parametrize(
    ('username'),
    (
        ('joe'),
        ('jeremy'),
        ('alice'),
        ('bob'),
        ('kruskal')
    )
)
def test_login(client, auth, username):
    auth.register(username=username) 
    auth.login(username=username)

    with client:
        client.get('/')    
        assert session['_user_id'] == username 

def test_index_contains_username(client, auth):
    auth.register()
    auth.login()

    res = client.get('/')
    assert res.status_code == 200
    assert 'test' in str(res.data)

@pytest.mark.parametrize(
    ('username', 'post_content'),
    (
        ('joe', 'i loves burgers'),
        ('alice', 'foobar')
    )
)
def test_create_post(client, auth, username, post_content):
    auth.register(username=username)
    auth.login(username=username)

    data = SimpleNamespace(
        text=post_content,
        submit='foo'
    )    
    form = CreatePostForm(formdata=None, obj=data)
    res = client.post('/createpost', data=form.data, follow_redirects=True)
    assert res.status_code == 200

    assert username in str(res.data)
    assert post_content in str(res.data)
