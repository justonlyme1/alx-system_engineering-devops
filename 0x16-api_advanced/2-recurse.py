#!/usr/bin/python3
"""Contain Recurse FUnction"""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by u/Ecstatic_Sea_1316)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Debugging: Print status code and response text
        print("Status Code:", response.status_code)
        print("Response Text:", response.text[:500])  # Print first 500 characters for debugging
        
        if response.status_code == 404:
            return None
        
        # Ensure the response is in JSON format
        if response.headers.get('Content-Type') != 'application/json; charset=UTF-8':
            print("Unexpected content type:", response.headers.get('Content-Type'))
            return None
        
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        
        return hot_list
    
    except requests.RequestException as e:
        # Print exception for debugging
        print("RequestException:", e)
        return None

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is None:
            print("None")
        else:
            for title in result:
                print(title)
