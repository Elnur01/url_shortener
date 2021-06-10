#import our library
import bitly_api

#define bitly token
BITLY_ACCESS_TOKEN = "29929fc8cb327c419d60ac7764d9521f63562042"

#Connect token with function
b = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)

#Shorten the link
response = b.shorten('http://google.com/')

#printing out short link :)
print(response)