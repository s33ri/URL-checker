# URL-checker
Small python script which takes a list of URL's from txt file and based on HTTP response, reflects back whether the URL is accessible or not e.g.- if server sends 200 OK/201 Created- script identifies that the URL is accessible

## Pre-requisites:-
* Install Python
* Install Python's "requests" library. If not, run the command - "pip install requests"
``` 
  In Windows you can find pip.exe under C:\Python27\Scripts
```
* Create a list of URL's in a txt file
```
   txt file Format:-
   Each URL in new line
   Each URL should be without http/https://
 ```

## Usage:-
This python script takes a txt file as an input from the user via command line argument and performs the check on all the URL's present in the file.

### Usage command - 
```
chmod +x script.py                  --- Grant execution privilege to script.py
./script.py url.txt                 --- makes sure script.py and url.txt are in the same directory
./script.py <path to the txt file>  --- url.txt is present in a different drectory than the script
 ```
## Screenshots:-

### Script Execution
  ![run](https://user-images.githubusercontent.com/40600860/41921749-2e143f26-7981-11e8-94bb-642557bcfabb.png)

### Sample txt file
  ![txt](https://user-images.githubusercontent.com/40600860/41922016-cfac26d2-7981-11e8-9b0d-9465c1e0da8a.png)
