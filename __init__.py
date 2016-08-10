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
import os
import gc # flask and garbage collection is not a good combo, clear session should invite a gc.collect()
from functools import wraps
from  datetime import datetime
import time
import sigma
import auth

le_key = '1337' # os.urandom(24)
app = Flask(__name__)   # obligatorisk 
app.secret_key = le_key


# ----------- LOGIN WRAP -----------

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'innlogget' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))
    return wrap


##################################################
# ------------- HTTP request ROUTES -------------#
# ---------------------------------------------- #
""" 
    Every route is defined like this 
    @app.route('/url')

    To access the function, you send a HttpRequest with this url
      http://www.domainname.com + /url 
                                        ----- Jonas ----- """

# ---------------- MISC ROUTES ---------------------

@app.route('/')
def index():
    # ryddig.
    if 'innlogget' in session:
        return redirect(url_for('input_url'))
    else:
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():

    session.clear()
    gc.collect()  
    return redirect(url_for('index'))


# --------- RENDER TEMPLATE view ROUTES ------------

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


@app.route('/maps')
@login_required
def maps():
    user = session['user']
    maps = sigma.get_maps(user).values()
    
    # adding the url pointing to each map, using url_for
    # (not implemented yet)
    
    
    return render_template('maps.html', maps=maps)


@app.route('/<user>/map/<mapid>')
@login_required
def show_map(user, mapid):
    # the url is built with user added to it to
    # be ready for the future when we might dare to
    # share our maps. 
    user = session['user']
    the_map = sigma.get_map(user, mapid)
    if the_map is None:
        return "There is no map with this main_topic"
    #the_map = sigma.KnowledgeMap("Python", "flask")
    return the_map.main_topic
 

# --------- FORM POST request ROUTES -----------------

@app.route('/postuser', methods=['POST'])
def post_user():

    user = request.form.get('iUser', None)
    if (auth.authenticate(user, None)):
        session['innlogget'] = True
        session['user'] = user
        session['last_request'] = time.time()

    return redirect(url_for('input_url'))


# ---------- AJAX POST/GET request ROUTES -------------

@app.route('/postmeta', methods=['POST'])
@login_required
def post_meta():
    user = session['user']
    json = request.get_json()

    meta = json['meta']
    url = json['url']

    if url and meta:
        # Saves it in the users links file.
        try:
            links = sigma.save_link(id=url, meta=meta, user=user)
            return jsonify(links=links, status='Postmeta OK')
        except Exception as e:
            return jsonify(status='Meta error:' + str(e))
    return 'Missing Url and Meta'


@app.route('/getmap', methods=['POST'])
@login_required
def get_map():

    user = session['user']

    try:
        mapid = request.form.get('main_topic', None)
        le_map = sigma.get_map(user, mapid) 

        return jsonify(status='Getmap OK: mapid: '+mapid, le_map=le_map)

    except Exception as e:
        return jsonify(status='Getmap error:' + str())


@app.route('/postmap', methods=['POST'])
@login_required
def post_map():

    user = session['user']

    try:
        le_map = json['le_map']
        mapid = json['main']

        sigma.save_map(user, mapid, le_map)
        return jsonify(status='Postmap OK')
    except Exception as e:
        return jsonify(status='Postmap error:' + str())




@app.route('/fetchtitle', methods=['POST'])
@login_required
def fetch_title():
    """ 
        time.clock() - returns a floating point number of time since epoch
                    in seconds. Accuracy in microseconds.  -- Jonas """
    try:
        now = time.time()
        elapsed = now - session['last_request']

        if elapsed <= 2: 
            return jsonify(title="Too fast!")
        
        url = request.form.get('url', None)
        title = sigma.fetch_title(url)
        session['last_request'] = time.time()

        return jsonify(title=title)

    except Exception as e:
        return jsonify(title="Server ERROR: " + str(e))


@app.route('/fetchmeta', methods=['POST'])
#@login_required
def fetch_meta():
    """ 
        Returns a filtered set of meta data about a given url.
        I.e:
            {
                meta: {
                    title: "A fish flying to the moon",
                    domain: "fishcanfly.com",
                    favicon: "https://fishcanfly.com/favicon.ico",
        
                    topics: {
                        cls1: {
                                Fish: 0.99999,
                                moon: 0.00001
                             },
                        success: True,
                        errorMessage: '',
                        version: '1.01',
                        textCoverage: 0.441786,
                        statusCode: 2000
                    }   
                }
            }                            -- Robin """
    try:
        now = time.time()
        elapsed = now - session['last_request']

        if elapsed <= 2: 
            return jsonify(status="Too fast!")

        session['last_request'] = time.time()
        url = request.form.get('url', None)
        filters = request.form.get('filter', None)
        # Not implemented filters yet. It dumps everything we got.
        meta = sigma.fetch_meta(url)
        # This will build a json response based on all the 
        # attributes in the LinkMeta object.
        return jsonify(meta=meta.__dict__, status="OK!")

    except Exception as e:
        return jsonify(status="Server ERROR: " + str(e))


@app.route('/fetchlinks', methods=['GET'])
@login_required
def fetch_links():
    user = session['user']
    try:
        links = sigma.get_links(user)
        return jsonify(links=links, status='OK')
    except Exception as e:
        return jsonify(status='Not OK - ' + str(e))

# ------------------------------------------------ #
# ------------------- LAST ROUTE ----------------- #
####################################################


if __name__ == '__main__':
    import webbrowser # Webbrowser makes you able to open browser with specified url.
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)

# EOF