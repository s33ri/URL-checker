# URL-status-identifier
Small python script which takes a list of URL's from txt file and based on HTTP response, reflects back whether the URL is accessible or not e.g.- if server sends 200 OK/201 Created- script identifies that the URL is accessible

Pre-requisites:-
1. Python is installed
2. Python's "requests" library is installed and up to date. If not, run the command - "pip install requests"

Usage:-
This python script takes a txt file as an input from the user via command line argument and performs the check on all the URL's present in the file.
Usage command - 
chmod +x script.py --- Grant execution privilege to script.py
./script.py url.txt --- makes sure script.py and url.txt are in the same directory
./script.py <path to the txt file>  --- url.txt is present in a different drectory than the script
  
Sample txt file content:-
(Each URL in a new line and without http/https://)

www.google.com
www.facebook.com
www.yahoo.com
123456
github.com
www.upwork.com/att/
