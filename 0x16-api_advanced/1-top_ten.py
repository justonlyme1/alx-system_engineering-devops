import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        # Check if the response is in JSON format
        if response.headers.get('Content-Type') == 'application/json; charset=UTF-8':
            try:
                data = response.json()
                results = data.get("data", {})
                children = results.get("children", [])

                if children:
                    for child in children:
                        print(child.get("data", {}).get("title", ""))
                else:
                    print("None")
            except ValueError:
                # Handle JSON decoding errors
                print("None")
        else:
            print("None")

    except requests.RequestException:
        # Handle network-related errors
        print("None")

