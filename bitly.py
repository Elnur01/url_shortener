#import our library
import bitly_api

#define bitly token
BITLY_ACCESS_TOKEN = "29929fc8cb327c419d60ac7764d9521f63562042"

#Get url from user/client
URL = input("URL that you want to shorten: ")

#Connect token with function
t = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)

#Shorten the link
response = t.shorten(URL)

#printing out short link :)
print(response)