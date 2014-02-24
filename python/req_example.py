import requests
access_token = 'CAACEdEose0cBAFunl1FMeOS9Ru8rkszqOXyuRcj0ZAtV9ORWpqWk5Ya9PiS5juKWmrGljVhOXvqIzUEEbrhcaYBE5KvN2KGYHdWtyikIk05ZB2aHY3mfTk2iDwDmMhlHqpHs0gchyZCiTqwJBhgio1eQVZA8gKtrkRL5ErVp6oVXB3ZA3AO0tKGWbgBSarzLk6iVW5ZBjmDAZDZD'
url = 'http//www.graph.facebook.com/fql'
params = {'access_token':access_token,
    'q':"SELECT name FROM user WHERE uid=me()"}
    
r = requests.get(url, params=params, data=params )
print r.text
r.status_code

