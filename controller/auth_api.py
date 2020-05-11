import jwt
from app.main.model.auth_users_db import connect_db
from flask import Flask, Blueprint, jsonify, request, session, make_response, render_template

index_blueprint = Blueprint('index', __name__)
login_blueprint = Blueprint('login', __name__)


@index_blueprint.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'currently  logged in'


@login_blueprint.route("/login", methods=["GET"])
def login():
    # Output message if something goes wrong...
    # msg = 'wrong username and password'
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using sqlite
        sqliteConnection = connect_db()
        cursor = sqliteConnection.cursor()
        cursor.execute('SELECT * FROM userdata WHERE username = ?  AND password = ? ', (username, password,))
        # Fetch one record and return result
        user = cursor.fetchone()
        # If account exists in accounts table in out database
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = user[0]
            session['password'] = user[1]
            token = jwt.encode({
                'user': request.form['username'],
                # 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=130)

            })
            # app.config['SECRET_KEY'])
            return jsonify({'token': token.decode('utf-8')})
        else:
            return make_response('unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "login required"'})

