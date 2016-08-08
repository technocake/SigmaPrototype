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

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)   # obligatorisk 





# EOF