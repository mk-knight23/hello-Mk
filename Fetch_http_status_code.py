#Program to fetch the http status code give the url/api
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import emoji

#Taking input url from user
requestURL = input("Enter the URL to be invoked: ")

#Gets the response from URL and prints the status code and message accordingly
try:
    response = urlopen(requestURL)
    #In case of success, prints success status code
    print('Status code : ' + str(response.code))
    print('Message : ' + 'Request succeeded. Request returned message - ' + response.reason)
except HTTPError as e:
    #In case of request failure, prints HTTP error status code
    print('Status : ' + str(e.code))
    print('Message : Request failed. Request returned reason - ' + e.reason)
except URLError as e:
    #In case of bad URL or connection failure, prints Win Error 
    print('Status :',  str(e.reason).split(']')[0].replace('[',''))
    print('Message : '+ str(e.reason).split(']')[1])
