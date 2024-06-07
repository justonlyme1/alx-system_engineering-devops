#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("None")
        return
    except requests.exceptions.RequestException as e:
        print("None")
        return

    try:
        results = response.json().get("data")
        if not results:
            print("None")
            return
        for post in results.get("children", []):
            print(post.get("data", {}).get("title"))
    except ValueError:
        print("None")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
