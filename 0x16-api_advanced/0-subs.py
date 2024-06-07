#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
  """Fetches the subscriber count for a subreddit from the Reddit API.

  Args:
      subreddit: The name of the subreddit (e.g., "programming").

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  # Build the API URL with a custom User-Agent to avoid throttling
  url = f"https://www.reddit.com/r/{subreddit}/about.json?raw_json=1"
  headers = {"User-Agent": "my_custom_user_agent"}

  try:
    # Send a GET request without following redirects
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Parse the JSON response
    data = response.json()

    # Check if the subreddit exists by looking for the "data" key
    if "data" in data and data["data"]:
      return data["data"]["subscribers"]
    else:
      return 0

  except requests.exceptions.RequestException:
    # Handle any errors that might occur during the request
    return 0

# Example usage (assuming 0-subs.py is saved in the same directory)
if __name__ == "__main__":
  import sys

  if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
    sys.exit(1)

  subreddit = sys.argv[1]
  subscribers = number_of_subscribers(subreddit)

  # Print success message based on subscriber count
  if subscribers > 0:
    print(f"OK - Subreddit '{subreddit}' has {subscribers} subscribers.")
  else:
    print(f"OK - Subreddit '{subreddit}' does not exist or is invalid.")
