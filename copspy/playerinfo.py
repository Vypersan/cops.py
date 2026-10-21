from turtle import st
from typing import TYPE_CHECKING, Any
from .errors import GenericError, PlayerNotFound, NoNetwork, RateLimited, Unauthorized, ResponseNotOK

if TYPE_CHECKING:
    from copspy.client import Client


class PlayerInfo:
    def __init__(self, client: "Client"):
        self.client = client

    def get_player_by_ign(
        self,
        players: str,
    ) -> dict[str, Any]:
        """Fetch player information by in-game name (IGN).

        Args:
            players: Comma-separated list of player IGN strings with a limit of 20.

        Returns:
            A dictionary containing the player's stats.

        Raises:
            PlayerNotFound: If the player does not exist.
            RateLimited: If the API rate limit is exceeded.
            Unauthorized: If authentication fails.
            ResponseNotOK: If the API request fails.
            GenericError: If another API error occurs.
        """
        try:
            response = self.client.request("GET", "/profile/", params={"usernames": players})
            return response
        except PlayerNotFound as e:
            print(f"One or more players not found in game. {players}. Error: {e}")
            return None
        except RateLimited as e:
            print(f"Rate limit exceeded while fetching player info for: {players}. Error: {e}")
            return None
        except Unauthorized as e:
            print(f"Unauthorized access while fetching player info for: {players}. Error: {e}")
            return None
        except ResponseNotOK as e:
            print(f"Failed to fetch player info for: {players}. Error: {e}")
            return None
        except GenericError as e:
            print(f"An error occurred while fetching player info for: {players}. Error: {e}")
            return None

    def get_player_by_uuid(self, uuid: str) -> dict[str, Any]:
        """Fetch profile statistics by UUID.
        
            Args:
                uuid: Comma-separated list of player UUID strings with a limit of 20.
        
            Returns:
                A dictionary containing the player's stats.
        
            Raises:
                PlayerNotFound: If the player does not exist.
                RateLimited: If the API rate limit is exceeded.
                Unauthorized: If authentication fails.
                ResponseNotOK: If the API request fails.
                GenericError: If another API error occurs.
            """
        try:
            response = self.client.request("GET", "profile/", params={"ids": uuid})
            return response
        except PlayerNotFound as e:
            print(f"One or more players not found in game. {uuid}. Error: {e}")
            return None
        except RateLimited as e:
            print(f"Rate limit exceeded while fetching player info for: {uuid}. Error: {e}")
            return None
        except Unauthorized as e:
            print(f"Unauthorized access while fetching player info for: {uuid}. Error: {e}")
            return None
        except ResponseNotOK as e:
            print(f"Failed to fetch player info for: {uuid}. Error: {e}")
            return None
        except GenericError as e:
            print(f"An error occurred while fetching player info for: {uuid}. Error: {e}")
            return None


    def get_user_weapon_stats(  
        self,
        uuid: str,
        game_type: int,
    ) -> dict[str, Any]:
        """Fetch weapon stats for a player.

        Args:
            uuid: The player's UUID.
            game_type: 1 for ranked, 2 for casual and custom.

        Returns:
            A dictionary containing the player's weapon stats.

        Raises:
            PlayerNotFound: If the player does not exist.
            RateLimited: If the API rate limit is exceeded.
            Unauthorized: If authentication fails.
            ResponseNotOK: If the API request fails.
            GenericError: If another API error occurs.
        """
        try:
            return self.client.request(
                "GET",
                "stats/weapons",
                params={
                    "user_id": uuid,
                    "game_type": game_type,
                },
            )
        except PlayerNotFound as e:
            print(f"One or more players not found in game. {uuid}. Error: {e}")
            return None
        except RateLimited as e:
            print(f"Rate limit exceeded while fetching player weapon stats for: {uuid}. Error: {e}")
            return None
        except Unauthorized as e:
            print(f"Unauthorized access while fetching player weapon stats for: {uuid}. Error: {e}")
            return None
        except ResponseNotOK as e:
            print(f"Failed to fetch player weapon stats for: {uuid}. Error: {e}")
            return None
        except GenericError as e:
            print(f"An error occurred while fetching player weapon stats for: {uuid}. Error: {e}")
            return None


    def get_player_matches(self, uuid: str) -> dict[str, Any]:
        """Fetch match history for a player.

        Args:
            uuid: The player's UUID.

        Returns:
            A dictionary containing the player's match history.

        Raises:
            PlayerNotFound: If the player does not exist.
            RateLimited: If the API rate limit is exceeded.
            Unauthorized: If authentication fails.
            ResponseNotOK: If the API request fails.
            GenericError: If another API error occurs.
        """
        try:
            return self.client.request(
                "GET",
                "matches/player",
                params={
                    "user_id": uuid,
                },
            )
        except PlayerNotFound as e:
            print(f"One or more players not found in game. {uuid}. Error: {e}")
            return None
        except RateLimited as e:
            print(f"Rate limit exceeded while fetching player matches for: {uuid}. Error: {e}")
            return None
        except Unauthorized as e:
            print(f"Unauthorized access while fetching player matches for: {uuid}. Error: {e}")
            return None
        except ResponseNotOK as e:
            print(f"Failed to fetch player matches for: {uuid}. Error: {e}")
            return None
        except GenericError as e:
            print(f"An error occurred while fetching player matches for: {uuid}. Error: {e}")
            return None


    def fetch_match(self, ids: str) -> dict[str, Any]:
        """Fetch details for a specific match.

        Args:
            ids: The match ID(s), comma-separated if multiple.

        Returns:
            A dictionary containing the match details.

        Raises:
            PlayerNotFound: If the player does not exist.
            RateLimited: If the API rate limit is exceeded.
            Unauthorized: If authentication fails.
            ResponseNotOK: If the API request fails.
            GenericError: If another API error occurs.
        """
        try:
            return self.client.request(
                "GET",
                f"matches/fetch",
                params={
                    "ids": ids,
                }
            )
        except PlayerNotFound as e:
            print(f"One or more players not found in game. {ids}. Error: {e}")
            return None
        except RateLimited as e:
            print(f"Rate limit exceeded while fetching match details for: {ids}. Error: {e}")
            return None
        except Unauthorized as e:
            print(f"Unauthorized access while fetching match details for: {ids}. Error: {e}")
            return None
        except ResponseNotOK as e:
            print(f"Failed to fetch match details for: {ids}. Error: {e}")
            return None
        except GenericError as e:
            print(f"An error occurred while fetching match details for: {ids}. Error: {e}")
            return None