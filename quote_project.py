                        '''  ✅ Beginner Version (Quote Fetcher)  ''' 

# =========== PROJECT 1 : QUOTE FETCHER ===========

import requests
import random

print("✅ Project 1 Started : Quote Fetcher !!")

# Defining Fallback Quotes :  

fallback_quotes = [

    {"content": "The expert in anything was once a beginner.", "author": "Helen Hayes"},
    {"content": "Doubt kills more dreams than failure ever will.", "author": "Suzy Kassem"},
    {"content": "Little by little, one travels far.", "author": "J.R.R. Tolkien"} 

]

# Function to Display Quote :

def show_quote(content, author, source = "API") :
    print(f"\n  Source: {source}")
    print(" 💬 " , content)
    print("✍️ - " , author) 
    

# Normal API Call :

try:
    response = requests.get("https://api.quotable.io/random")
    response.raise_for_status()
    data = response.json()

    show_quote(data["content"], data["author"])

except requests.exceptions.RequestException as e :
    print("\n ⚠️ Network/API Error:", e)
    backup = random.choice(fallback_quotes)
    show_quote(backup["content"], backup["author"], "Fallback Quote") 


# Wrong URL Test :  

try:
    response = requests.get("https://api.quotable.iiio/random")         # Wrong URL
    response.raise_for_status()
    data = response.json()

    show_quote(data["content"], data["author"])

except requests.exceptions.RequestException:
    print("\n ⚠️ API Error (Wrong URL)")
    backup = random.choice(fallback_quotes)
    show_quote(backup["content"], backup["author"], "Fallback Quote") 


# Wrong Key Test :

try:
    response = requests.get("https://api.quotable.io/random")
    response.raise_for_status()
    data = response.json()

    # Purposely using wrong keys 

    show_quote(data["contenttt"], data["authorr"])

except (KeyError, requests.exceptions.RequestException):
    print("\n ⚠️ Key Error : Wrong key used")
    backup = random.choice(fallback_quotes)
    show_quote(backup["content"], backup["author"], "Fallback Quote") 


# Different Endpoint :

try:
    response = requests.get("https://api.quotable.io/quotes")  # Different endpoint
    response.raise_for_status()
    data = response.json()

    # Here data structure is different (list of quotes instead of one) 

    first_quote = data["results"][0]   # Take first from list
    show_quote(first_quote["content"], first_quote["author"])

except (KeyError, requests.exceptions.RequestException):
    print("\n ⚠️ API unavailable / Different structure")
    backup = random.choice(fallback_quotes)
    show_quote(backup["content"], backup["author"], "Fallback Quote")


