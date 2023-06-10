from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # name = request.form['name']
        print(request.form)
        # email = request.form['email']
        # password = request.form['password']
        # print(name)
        # print(email)
        # print(email)
        pass
        return render_template('register.html')
    if request.method == 'GET':
        pass
        return render_template('register.html')
    
    
    

@app.route('/testForm', methods=['GET', 'POST'])
def func_name():
    print(request.form['fname'])
    return render_template('testForm.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        return render_template('login.html')
    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 