users = {}

def login(username, password):
    if username == None or password == None:
        return False
    return password == users.get(username)

def create():
    pass
def delete():
    pass
def save():
    pass