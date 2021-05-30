Overview

Jormungandr is a web spider application currently only for kali linux that obscures the 
Computer the user works from to allow for more anonymity. The application is comprised 
of a bash shell script along with a python file and does require that you have python3 
installed in order to run. The python file randomly changes the MAC and IP address of 
the users wifi interfaces each time the application is launched, so that it's harder to 
trace exactly where the source of the users terminal is located in the world. The 
application is an addon of a prebuilt kali application called gospider, that utilizes 
all the aspects of the application in order to give the user a better understanding of 
the target website they are attempting to map. This application is in no way to be 
intended to be malicious, and the users who copy this repository are responsible for 
all actions on their part.


Installation of requirements.txt

To install all the requirements necissary for the use of jormungandr run the following:

"pip install -r requirements.txt"


Install of commandline tools

To install the commandline tools needed for Jormungandr run the following commands:

"sudo chmod u+x cmdR"
"sudo ./cmdR"


Running Jormungandr:

In order to run the app you must first change the permissions of both the python file main
and the bash file disguise:

"sudo chmod u+x main.py && sudo chmod u+x disguise"

After you have changed the permissions simply run:

"sudo ./disguise"

and follow the prompts following. Simple!


Upcoming updates to Jormungandr

Currently the application is set in stone as the user can only input the website they
wish to map and where they'd like to store the data that gospider collects. It's also
only really meant to be run on kali linux and similar distributions. In a future
update to the application, the user will not only have these options but also the choise of
what web platform they would like to use (currently tor for max anonymity), the number of
active threads that they would like to run at the same time, the max depth of the domain they
are targeting(currently set to 0 for unlimited), choice of random delay, choice of if
they would like to search for the sitemap(xml) file or if they would only like the domains 
connected domains and subdomains in connection to the main domain entered at the start of the
application, choice of finding 3rd party domains in connection with the target domain, choice
of including subdomains, as well as the choice of having the application show or not show
its progress with the verbose option(currently set to True). 
