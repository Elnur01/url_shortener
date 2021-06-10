#import our library
import pyshorteners

#Get url from user/client
url = input("Enter your url: ")

#printing out short link :)
print("Your url: ", pyshorteners.Shortener().tinyurl.short(url))