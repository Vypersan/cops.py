# cops.py

`copspy` is a Python client for the public Critical Ops API. It provides a small interface for looking up player profiles, player weapon statistics, and match data.

This is an unofficial, fan-made project. It is not affiliated with, endorsed by, or connected to Critical Force Oy, Critical Ops, or any related company.

## Installation

Install the package from PyPI:

```bash
python -m pip install copspy
```

## Requirements

- Python 3.10 or later
- A valid Critical Ops public API token

## Authentication

Pass your API token when creating a client:

```python
from copspy.client import Client

client = Client(token="YOUR_API_TOKEN")
```

Alternatively, set the `COPS_API_TOKEN` environment variable before starting Python, then omit the `token` argument:

```powershell
$env:COPS_API_TOKEN = "YOUR_API_TOKEN"
```

```bash
export COPS_API_TOKEN="YOUR_API_TOKEN"
```

```python
from copspy.client import Client

client = Client()
```

Do not commit API tokens to source control. Prefer configuring the environment variable outside your application code for deployed applications.

## Quick start

Use the client as a context manager so its HTTP session is closed when you are finished:

```python
from copspy.client import Client

with Client() as client:
    profile = client.playerinfo.get_player_by_ign("player_name")
    print(profile)
```

`Client` also accepts optional `base_url`, `timeout`, `retries`, and `retry_delay` arguments. The default API base URL is the Critical Ops public API, and the default request timeout is 30 seconds. The API occasionally returns a spurious `404 Endpoint Not Found.`, so the client retries those responses up to `retries` times (default 5), waiting `retry_delay` seconds (default 0.5) between attempts.

## Available methods

All methods below are accessed through `client.playerinfo`.

### Player profiles

Look up a player by in-game name (IGN):

```python
profile = client.playerinfo.get_player_by_ign("player_name")
```

Look up a player by UUID:

```python
profile = client.playerinfo.get_player_by_uuid("player-uuid")
```

The profile lookup methods accept comma-separated names or UUIDs, respectively, with a maximum of 20 values per request:

```python
profiles = client.playerinfo.get_player_by_ign("player_one,player_two")
profiles = client.playerinfo.get_player_by_uuid("uuid-one,uuid-two")
```

### Weapon statistics

Fetch weapon statistics for a player UUID. Use `game_type=1` for ranked or `game_type=2` for casual and custom:

```python
weapon_stats = client.playerinfo.get_user_weapon_stats(
    uuid="player-uuid",
    game_type=1,
)
```

### Match data

Fetch a player's match history:

```python
matches = client.playerinfo.get_player_matches("player-uuid")
```

Fetch details for one or more match IDs:

```python
match_details = client.playerinfo.fetch_match("match-id")
```

`fetch_match` accepts comma-separated match IDs.

## Responses and errors

Successful calls return the JSON response from the API. The player-info helper methods print an error message and return `None` if a request fails; check for `None` before using the result. The lower-level `Client.request` method raises error types defined in `copspy.errors`, including `PlayerNotFound`, `RateLimited`, `Unauthorized`, `ResponseNotOK`, and `GenericError`. If the API keeps answering `Endpoint Not Found.` after all retries, `ResponseNotOK` is raised rather than `PlayerNotFound`.

The API may apply rate limits or change its responses. Handle missing data and failed requests in your application.

## License

This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt).

## Credits

Developed by [VyPER](https://github.com/VyperSan).
