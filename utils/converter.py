#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
	File       : converter.py
	Description: This is a converter. 

"""
import sys
import re

#GUI imports


from tkinter import *
from tkinter import filedialog
import tkinter

import tkinter.messagebox
#import tkFileDialog

def slice_string(toslice):
	return toslice.split("/")[-1]


def convert(file, path):

	#Have to figure out how to delete last comma in end_file

	freemind_file = open(file, 'r')

	if path != None:
		name = path + "/" + slice_string(file)
	else: 
		name = freemind_file.name

	name = name[:-2]
	name = name + "json"

	json_file = open(name, 'w')
	done = True
	just = False

	for line in freemind_file:
		if line.startswith('<node CREATED='):
			text1 = re.search('TEXT="(.+?)"', line).group()
			text2 = re.search('"(.+?)"', text1).group()

			if "/>" in line:
				if done == False:
					json_file.write(',\n')
				
				line_towrite = '{"resource":' + str(text2) + "}"
				json_file.write(line_towrite)
				
				done = False
			
			else:
				line_towrite = '{' + str(text2) + ':[\n'
				json_file.write(line_towrite)
				done = True
				just = False

		elif line.startswith('</node>'):
			#How to delete last comma in end_file
			if done == False:
				if just == False:
					json_file.write("\n]},\n")
					just = True
				else: 
					json_file.write("]},\n")
			else:
				json_file.write("]},\n")

	return json_file.name + " created."

def gui():

	#window
	top = tkinter.Tk()

	#callbacks
	def choosefile_callback():
   		#tkinter.messagebox.showinfo( "Convert", "Convert") #1st convert = title
   		filename = filedialog.askopenfilename(initialdir = "/", title = "Select freemind file", filetype=(("Freemind maps", "*.mm"),("All files", "*.*")))
   		print(filename)
   		update_status_filename(slice_string(filename))

	def choosedir_callback():
   		directory = filedialog.askdirectory(initialdir = "/", title = "Select destination folder", mustexist=True)
   		update_status_directory(directory)

	def convert_callback():
		if status_filename["text"] != "None":
			if ".mm" in status_filename["text"]:
				path_send = None
				if status_directory["text"] != "default = current directory":
					path_send = status_directory["text"]

				update_status_msg(slice_string(convert(status_filename["text"], path_send)))
				update_status_filename("None")
				update_status_directory("default = current directory")
			else:
				tkinter.messagebox.showinfo("Error", "This file type is not supported")
		else:
			tkinter.messagebox.showinfo( "Error", "No file has been selected.")


	#Updates to update the different statuses
	def update_status_filename(update_filename):
		status_filename["text"] = update_filename

	def update_status_directory(update_directory):
		status_directory["text"] = update_directory

	def update_status_msg(update_msg):
		status_msg["text"] = update_msg

	#status
	status_filename = tkinter.Label(top, text="None")
	status_directory = tkinter.Label(top, text="default = current directory")
	status_msg = tkinter.Label(top, text="")

	#buttons
	choosefile_button = tkinter.Button(top, text ="Choose file", command = choosefile_callback)
	choosedir_button = tkinter.Button(top, text ="Destination", command = choosedir_callback)
	convert_button = tkinter.Button(top, text ="Convert", command = convert_callback)

	#mapping layout
	#row1
	status_filename.grid(row=1, column=1)
	choosefile_button.grid(columnspan=2,row=1, column=2)
	#row2
	status_directory.grid(row=2, column=1)
	choosedir_button.grid(columnspan=2, row=2, column=2)
	#row3
	convert_button.grid(columnspan=4, row=3)
	#row4
	status_msg.grid(columnspan=4, row=4)


	top.mainloop()


destination_bool = False
file_bool = False

try:
	if sys.argv[1] != None:
		file_bool = True
except:
	file_bool = False

try:
	if sys.argv[2] != None:
		destination_bool = True
except:
	destination_bool = False

if file_bool == True:
	if ".mm" in sys.argv[1]:
		if destination_bool == True:
			print(convert(sys.argv[1], sys.argv[2]))
		else:
			print(convert(sys.argv[1], None))
	else:
		print("This file type is not supported")
else:
	gui()
