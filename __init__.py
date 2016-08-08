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

app = Flask(__name__)   # obligatorisk 


""" Every route is defined like this 
    @app.route('/url')

    To access the function, you send a HttpRequest with this url
      http://www.domainname.com + /url 
                                        ----- Jonas ----- """

@app.route('/')
def index():
    # ryddig.
    return redirect(url_for('input_url'))


@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/meny')
def meny():

    return render_template('base.html')

@app.route('/inputurl')
def input_url():

    return render_template('input.html')

@app.route('/posturl', methods=['POST'])
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
    

@app.route('/viewurl')
def view_links():
    user='technocake'
    links = sigma.get_links(user)
    return render_template('search.html', links=links)


# ---------- JAVASCRIPT AJAX ROUTES -------------

@app.route('/fetchtitle', methods=['POST'])
def fetch_title():

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