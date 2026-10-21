import os, time, requests
from copspy import errors


class Client:
    def __init__(
        self,
        token: str | None = None,
        base_url: str = "https://default.prod.copsapi.criticalforce.fi/api/public/v2/",
        timeout: float = 30.0,
        retries: int = 5,
        retry_delay: float = 0.5,
    ):
        self.token = token or os.getenv("COPS_API_TOKEN")
        if not self.token:
            raise ValueError(
                "API TOKEN is required. Either set it by filling in the token parameter or by setting the COPS_API_TOKEN environment variable."
            )

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.retry_delay = retry_delay
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
        )

        from .playerinfo import PlayerInfo

        self.playerinfo = PlayerInfo(self)

    def request(self, method: str, endpoint: str, **kwargs):

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        for attempt in range(self.retries + 1):
            try:
                response = self.session.request(
                    method,
                    url,
                    timeout=self.timeout,
                    **kwargs,
                    headers=self.session.headers,
                )
            except requests.RequestException as e:
                raise errors.GenericError(f"Request failed: {e}")
            # The API intermittently answers 404 "Endpoint Not Found." for valid routes.
            if (
                response.status_code == 404
                and response.text.strip() == "Endpoint Not Found."
                and attempt < self.retries
            ):
                time.sleep(self.retry_delay)
                continue
            break

        if not response.ok:
            if response.status_code == 404:
                if response.text.strip() == "Endpoint Not Found.":
                    raise errors.ResponseNotOK(
                        f"Endpoint not found (the API may be temporarily unavailable): {response.text}"
                    )
                raise errors.PlayerNotFound(f"Player not found: {response.text}")
            if response.status_code == 429:
                raise errors.RateLimited(f"Rate limit exceeded: {response.text}")
            if response.status_code == 401:
                raise errors.Unauthorized(f"No token / token invalid: {response.text}")
            if response.status_code == 500:
                raise errors.ResponseNotOK(
                    f"Internal server error. {response.status_code}: {response.text}"
                )
            if response.status_code == 400:
                raise errors.ResponseNotOK(
                    f"Bad request. {response.status_code}: {response.text}"
                )
            if response.status_code == 403:
                raise errors.Unauthorized(f"Forbidden: {response.text}")
            if response.status_code == 503:
                raise errors.ResponseNotOK(
                    f"Service unavailable. {response.status_code}: {response.text}"
                )
            else:
                raise errors.ResponseNotOK(
                    f"Response returned with status code {response.status_code}: {response.text}"
                )

        if response.status_code == 204 or not response.content:
            return None
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as exc:
            raise errors.GenericError("API returned invalid JSON.") from exc

    def close(self):
        print("Closing client session.")
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
