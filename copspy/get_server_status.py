import requests
from copspy import api_urls
from requests.exceptions import ConnectionError as cnerr
from copspy.apierror import NoNetwork, ResponseNotOK

headers = {
    "content-type": "application/json",
}

def get_all():
    """Get a list of all servers. Returns in json format."""
    try:
        json_servers = requests.get(api_urls.servers_api_url, headers=headers)
        if json_servers.ok:
            return json_servers.json()
        else:
            raise ResponseNotOK()
    except cnerr:
        raise NoNetwork()
