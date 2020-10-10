from app.models.user import User

def test_user():
    name = "Alan"
    email = "alanpjohn@outlook.com"
    k = User(name,email)
    assert(name == k.name and k.email == email)