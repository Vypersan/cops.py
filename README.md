# cops.py
copspy is a python API wrapper for the public version of the Critical Ops API.
This project is not affiliated with c-ops, Critical Force, Critical Force Oy or any related company.
This project is purely made for fun by the community and for the community.

# Install:
```bash
  python -m pip install u-copsapi
```

# Import
```python
  from copspy import get_profile
  from copspy.errors import apierror # For error handling
```

# Get user(s):
```python
# Get a player profile:
from copspy import get_profile
get_profile.get_player_by_ign("username here")

get_profile.get_player_by_id("id here")
```

# Getting multiple users
You can provide multiple usernames or ids.As long as you separate them with a `,` Such as: 
```python
get_profile.get_player_by_ign("usernme1, username2")


# or
get_profile.get_player_by_id("1234, 5678")
```


# Get server status:

```python
from copspy import get_server_status
# Get all servers
get_server_status.get_all()

```

# Developed by:
[VyPER](https://github.com/VyperSan)