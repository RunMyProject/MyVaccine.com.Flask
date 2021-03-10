from flask import Flask, render_template, json, request

from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView
from models import db_session

from schema import schema, Hospitalward, Patient
from models import Base

from sqlalchemy.orm import Query

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/showMyVaccineSpace')
def showMyVaccineSpace():
    return render_template('myvaccinespace.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    # read the posted values from the UI
    #
    _name = request.form['inputName']
    _password = request.form['inputPassword']

    # validate the received values
    #
    if _name and _password:
        query_string = '{patient(name:"'+ _name + '") { name password }}'

        # we can query for name and password fields
        #
        result = schema.execute(query_string)
        if(len(result.data['patient'])==0):
            return json.dumps({'warning':'<span>Username not found!</span>'})
        password = result.data['patient'][0]['password']
        if(password!=_password):
            return json.dumps({'warning':'<span>Password error!</span>'})
        return json.dumps({'message':'OK'})
    else:
        return json.dumps({'warning':'<span>Enter the required fields</span>'})

@app.route('/signIn',methods=['POST'])
def signIn():
    # read the posted values from the UI
    #
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    #
    if _name and _email and _password:
        return json.dumps({'warning':'<span>TODO!</span>'})
    else:
        return json.dumps({'warning':'<span>Enter the required fields</span>'})

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')

@app.route('/main')
def _main():
    return render_template('index.html')

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
