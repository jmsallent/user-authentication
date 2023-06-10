
import controller
import random



def test_registerUser():
   name = "test_name"
   email = "test_email"
   password = "test_password"
   controller.registerUser(name, email, password)

def test_loginUser():
   random_number = random.randint(0,9)
   name = "test_name" + str(random_number)
   email = "test_email" + str(random_number)
   password = "test_password" + str(random_number)
   controller.registerUser(name, email, password)
   controller.loginUser(email, password)