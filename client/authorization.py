from ast import arg
import minecraft_launcher_lib
import json
import threading
import os

CLIENT_ID = "dd82773a-d6be-47c6-82f7-30ff816cb255"
CLIENT_SECRET = "AjN8Q~Ymlosb4wzUJDjqQpMH9Jr6RWWeF49Shdn9"
REDIRECT_URI = "https://localhost/web-aerial"

def get_login():
    return minecraft_launcher_lib.microsoft_account.get_login_url(CLIENT_ID, REDIRECT_URI)

def login_complete(login_url):
    if not minecraft_launcher_lib.microsoft_account.url_contains_auth_code(login_url):
        print("the url occur the error, has some problem")
        return None
    auth_code = minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(login_url)
    login_data = minecraft_launcher_lib.microsoft_account.complete_login(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                            redirect_uri=REDIRECT_URI, auth_code=auth_code)
    file_path = "./client/data/login_data.json"
    
    try:
        if not os.path.exists('./client/data'):
            os.makedirs('./client/data')
    except:
        print("Error: Failed to create the directory")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(login_data, file, indent="\t")
    
    REFRESH_TOKEN = login_data.get("refresh_token")
    
    minecraft_launcher_lib.microsoft_account.complete_refresh(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                              redirect_uri=REDIRECT_URI, refresh_token=REFRESH_TOKEN)
    
def threading_login(login_url):
    t = threading.Thread(target=login_complete, args=(login_url,))
    t.start()
    
def has_login_data():
    try:
        path = "./client/data/login_data.json"
        return os.path.exists(path=path)
    except:
        print("ERROR : we cannot find any path login data")
        return False
    
