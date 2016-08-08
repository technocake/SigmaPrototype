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
"""

from flask import Flask, render_template, request, url_for, redirect
import pickle

app = Flask(__name__)   # obligatorisk 



@app.route('/')
def index():
	# ryddig.
	return redirect(url_for('inputurl'))

@app.route('/login')
def login():

	return render_template('login.html')

@app.route('/meny')
def meny():

	return render_template('base.html')

@app.route('/inputurl')
def input_url():

	return render_template('input.html')


@app.route('/viewurl')
def view_links():
	
	return render_template('search.html')


if __name__ == '__main__':
	import webbrowser
	webbrowser.open("http://localhost:5000")
	app.run(debug=True)

# EOF