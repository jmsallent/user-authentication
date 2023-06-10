import db

def registerUser(name, email, password):
    try:
        ross = db.User(email='ross@example.com')
        ross.first_name = 'Ross'
        ross.last_name = 'Lawley'
        ross.save()
    except:
        print("An exception occurred")
    

def loginUser(email, password):
    try:
        # products.objects(Name='TV'):
        pass
        
    except:
        print("An exception occurred")