from flask import Flask, render_template, request
from controller import registerUser , loginUser
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        registerUser(name, email, password);
        pass
        return render_template('succes_registration.html')
    if request.method == 'GET':
        pass
        return render_template('register.html')
    
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('succes_registration.html')
        pass
    if request.method == 'GET':
        return render_template('login.html')
    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
 