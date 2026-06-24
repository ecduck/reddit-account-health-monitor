import os
import requests
from dotenv import load_dotenv


load_dotenv()


CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USERNAME = os.getenv("REDDIT_USERNAME")
PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")


def get_access_token():
    if not all([CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, USER_AGENT]):
        raise RuntimeError("Missing required environment variables.")

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
    }

    headers = {
        "User-Agent": USER_AGENT,
    }

    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=auth,
        data=data,
        headers=headers,
        timeout=20,
    )

    response.raise_for_status()
    return response.json()["access_token"]


def fetch_me(access_token):
    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": USER_AGENT,
    }

    response = requests.get(
        "https://oauth.reddit.com/api/v1/me",
        headers=headers,
        timeout=20,
    )

    response.raise_for_status()

    return {
        "data": response.json(),
        "rate_limit": {
            "used": response.headers.get("X-Ratelimit-Used"),
            "remaining": response.headers.get("X-Ratelimit-Remaining"),
            "reset": response.headers.get("X-Ratelimit-Reset"),
        },
    }


def main():
    token = get_access_token()
    result = fetch_me(token)

    account = result["data"]

    print("Username:", account.get("name"))
    print("Link karma:", account.get("link_karma"))
    print("Comment karma:", account.get("comment_karma"))
    print("Verified email:", account.get("has_verified_email"))
    print("Rate limit:", result["rate_limit"])


if __name__ == "__main__":
    main()
