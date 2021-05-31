Overview

Jormungandr is a web spider application currently only for kali linux that obscures the 
Computer the user works from to allow for more anonymity while crawling and returning 
websites in the form of a text file. The application is comprised of two python files 
as well as an experimental bash file for faster response times. Jormungandr requires 
that you have python3 installed in order to run. The python file randomly changes the 
MAC and IP address of the users wifi interfaces each time the application is launched, 
so that it's harder to trace exactly where the source of the users terminal is located 
in the world. The application is an addon of a prebuilt kali application called 
gospider, that utilizes all the aspects of the application in order to give the user a 
better understanding of the target website they are attempting to map. This application 
is in no way to be intended to be malicious, and the users who copy this repository are 
responsible for all actions on their part.


Installation of requirements.txt

To install all the requirements necissary for the use of jormungandr run the following:

"pip install -r requirements.txt"


Install of commandline tools

To install the commandline tools needed for Jormungandr run the following commands:

"sudo chmod u+x cmdR"
"sudo ./cmdR"


Running Jormungandr:

In order to run the app you must first change the permissions of both the python file main:

"sudo chmod u+x main.py && sudo chmod u+x jormungandr"

After you have changed the permissions simply run:

"sudo pytho3 jormungandr"

and follow the prompts following. Simple!


Upcoming updates to Jormungandr

Currently the application is only meant for kali linux and run with python. There
is an experimental bash file which is still being worked on to make the response
of the program much faster than the python file can perform at. The jormungandr
python file will also be worked on to increase response time while the bash
file is still under construction. 
