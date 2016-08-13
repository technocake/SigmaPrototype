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
                                         ----- Jonas -----


#  --------------- URL INDEX ----------------------

    1.  /    
    2.  /logout 
    3.  /login
    4.  /meny 
    5.  /inputurl
    6.  /maps
    7.  /<user>/map/<mapid>
    8.  /<user>/map/<mapid>/thumbnail
    9.  /postuser
    10. /postmeta
    11. /getmap
    12. /mapnames
    13. /updatemap
    14. /relabeltopic
    15. /tags
    16. /deletelink
    17. /fetchtitle
    18. /fetchmeta
    19. /fetchlinks

# -------------------------------------------------   
"""

from flask import Flask, render_template, request, url_for, \
                   redirect, session, jsonify
import os
import gc # flask and garbage collection is not a good combo, clear session should invite a gc.collect()
from functools import wraps
from  datetime import datetime
import time
import sigma
# for pickles sake...
from sigma import KnowledgeMap, Topic
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
    return render_template('map.html', map=the_map)
 

@app.route('/<user>/map/<mapid>/thumbnail')
@login_required
def map_thumbnail(user, mapid):
    # the url is built with user added to it to
    # be ready for the future when we might dare to
    # share our maps.
    user = session['user']
    the_map = sigma.get_map(user, mapid)
    if the_map is None:
        return "There is no map with this main_topic"
    #the_map = sigma.KnowledgeMap("Python", "flask")
    return render_template('mapthumbnail.html', mapid=mapid)


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
    # POSTparamter is json = {url: '', meta : {<object>metainfo}}
    
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
        the_map = sigma.get_map(user, mapid) 

        return jsonify(status='Getmap OK', map=the_map.__dict__)

    except Exception as e:
        return jsonify(status='Getmap error:' + str(e))



@app.route('/getmaps', methods=['GET'])
@login_required
def get_maps():
    # NOT IMPLEMETNED, JSON SERIALIZING tecghnique missing.
    user = session['user']
    
    try:
        maps = sigma.get_maps(user) 
        return jsonify(status='Getmaps OK', map=maps)

    except Exception as e:
        return jsonify(status='Getmaps error:' + str(e))



@app.route('/mapnames', methods=['GET'])
@login_required
def get_map_names():

    user = session['user']
    try:
        the_maps = sigma.get_maps(user)

        map_names = []
        for k in the_maps:
            map_names.append(k)

        return jsonify(status='Names OK', names=map_names)

    except Exception as e:
        return jsonify(status='Names error:' + str(e))



@app.route('/updatemap', methods=['POST'])
@login_required
def update_map():
    # POSTparamter is json = {url: '', main_topic: '', subtopic: ''}

    user = session['user']
    json = request.get_json()
 
    try:
        url = json.get('url', None)
        main_topic = json['main_topic']
        subtopic = json['subtopic']

        new = sigma.update_map(user, main_topic, subtopic, url)
        return jsonify(status='Updatemap OK', new=new)
    except Exception as e:
        return jsonify(status='Updatemap error:' + str(e))


@app.route('/relabeltopic', methods=['POST'])
@login_required
def relabel_topic():
    user = session['user']
    json = request.get_json()

    try:
        map_id = json.get('map_id', None)
        old_topic = json['old']
        new_topic = json['new']

        sigma.relabel_topic(user, map_id, old, new)
        return jsonify(status='OK')
    except Exception as e:
        return jsonify(status='NOT OK', error="error: " + str(e))


@app.route('/fetchsearchdata', methods=['POST'])
@login_required
def fetch_searchdata():
    user = session['user']
    json = request.get_json()

    try:
        searchdata = sigma.get_searchdata(user)
        return jsonify(status='OK', searchdata=searchdata)
    except Exception as e:
        return jsonify(status='NOT OK', error="error: " + str(e))










######  -----   TAGS    -----   #######

@app.route('/tags', methods=['GET'])
@login_required
def get_tags():
    user = session['user']
    try:
        tags = sigma.get_tags(user)
        return jsonify(status='OK', tags=tags)
    except Exception as e:
        return jsonify(status='NOT OK', error="error: " + str(e))




@app.route('/deletelink', methods=['POST'])
@login_required
def delete_link():
    """
        Deletes a link from a a map, at a given subtopic node.
    """

    user = session['user']
    json = request.get_json()

    try:
        map_id = json.get('map_id', None)
        subtopic = json['subtopic']
        url = json['url']

        sigma.delete_link(user, map_id, subtopic, url)
        return jsonify(status='OK')
    except Exception as e:
        return jsonify(status='NOT OK', error="error: " + str(e))




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
        return jsonify(status='Not OK - ', error="error: " + str(e))

# ------------------------------------------------ #
# ------------------- LAST ROUTE ----------------- #
####################################################


if __name__ == '__main__':
    import webbrowser # Webbrowser makes you able to open browser with specified url.
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)

# EOF