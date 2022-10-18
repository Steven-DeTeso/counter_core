from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = '1234ABCD' # need to add everytime we use session. 

@app.route('/') #routes to the main page 'index.html
def index():
    if 'counter' not in session: #if no cookies have been made yet. This sets counter to 0 which is also Jinja coded into the index.html and displayed to the user. 
        session['counter'] = 0
        print("Key 'counter' does NOT exist, it was reset by ./destroy_session clicked")
    else: # triggers if session is in affect and incremnts the Jinja session by 1 int. 
        session['counter'] += 1
        print("Key 'counter' already or NOW exists!")
    return render_template('index.html')

@app.route('/destroy_session') #this is the href route coded into the reset button in html
def redirect_home():
    session.clear() # this built in function clear's session then redirects to the home html page below
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)