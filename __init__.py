#!usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Navn: __init__.py
    Prosjekt: SigmaPrototype
    Opprettet av: Jonas
    Beskrivelse: __init__.py fungerer som kontroller for hele Flask-applikasjonen.
                 En kontroller får input/request i form av en URL, f.eks www.google.com,
                  fra en klient. Kontrolleren bestemmer hva som skal returneres til klienten
                   for en gitt request.
                                         ----- Jonas ----- """

from flask import Flask, render_template, request, url_for, \
                   redirect, session, jsonify
import sigma
import auth
from functools import wrap


from  datetime import datetime

app = Flask(__name__)   # obligatorisk 


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'innlogget' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))
    return wrap


""" Every route is defined like this 
    @app.route('/url')

    To access the function, you send a HttpRequest with this url
      http://www.domainname.com + /url 
                                        ----- Jonas ----- """

@app.route('/')
def index():
    # ryddig.
    if 'innlogget' in session:
        return redirect(url_for('meny'))
    else:
        return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/meny')
@login_required
def meny():

    return render_template('base.html')

@app.route('/inputurl')
@login_required
def input_url():

    return render_template('input.html')
    
@app.route('/viewurl')
@login_required
def view_links():
    user='technocake'
    links = sigma.get_links(user)
    return render_template('search.html', links=links)

@app.route('/posturl', methods=['POST'])
@login_required
def post_url():
    user="technocake"
    url = request.form.get('iUrl', None)
    if url:
        # Saves it in the users links file.
        try:
            sigma.save_link(url=url, user=user)
            return 'OK'
        except:
            return 'NOT OK'

@app.route('/postuser')
@login_required
def post_user():

    user = request.form.get('iUser', None)
    session['innlogget'] = auth.authenticate(user, None)

    return redirect(url_for('meny'))


# ---------- JAVASCRIPT AJAX ROUTES -------------

@app.route('/fetchtitle', methods=['POST'])
@login_required
def fetch_title():
    last_request = session.get('last_request', datetime.now())

    try:
        url = request.form.get('iUrl', None)
        title = sigma.fetch_title(url)

        return jsonify(title=title)

    except Exception as e:
        return jsonify(result="Server ERROR: " + str(e))



if __name__ == '__main__':
    import webbrowser # Webbrowser makes you able to open browser with specified url.
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)

# EOF