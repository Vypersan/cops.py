import requests
from copspy import api_urls
from copspy import apierror
from requests.exceptions import ConnectionError as cnerr
from urllib3.exceptions import NameResolutionError
def get_player_by_ign(ign: str = None):
    """Get a profile and it's associated data like ID, xp, ranked stats, custom games stats."""
    headers = {
        "content-type": "application/json",
    }
    try:
        response = requests.get(url=api_urls.username_api_uri.__add__(ign), headers=headers)
        if response.ok:
            json_response = response.json()
            return json_response
        if response.status_code == 500:
            raise apierror.PlayerNotFound()
        
        elif response.status_code != 200:
            print(response.status_code)
            raise apierror.ResponseNotOK(response_text=response.content)
        
    except cnerr  as e:
       raise apierror.NoNetwork()


    

def get_player_by_id(id: int = None):
    """Get a profile and it's associated data like ID, xp, ranked stats, custom games stats."""
    headers = {
        "content-type": "application/json",
    }
    try:
        response = requests.get(url=api_urls.id_api_url.__add__(id), headers=headers)
        if response.ok:
            json_response = response.json()
            return json_response
        if response.status_code == 500:
            raise apierror.PlayerNotFound()
        elif response.status_code != 200:
            raise apierror.ResponseNotOK(response_text=response.content)
    except cnerr  as e:
       raise apierror.NoNetwork()

