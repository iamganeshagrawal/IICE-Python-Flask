#!/usr/bin/python3.6

print("Content-Type: text/html\n")

import cgi

form = cgi.FieldStorage()

nl = "<br/><br/>"

name = form.getvalue("name")
password = form.getvalue("password")
gender = form.getvalue("gender")
course = form.getvalue("course")

print(form, nl)
print(name, nl)
print(course, nl)