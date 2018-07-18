import json
import time
import sys

import praw
import requests
from prawcore.exceptions import ResponseException


def get_config():
    """Returns the configuration file."""
    with open("config.json") as f:
        return json.load(f)


def get_reddit(client_id, client_secret):
    """Returns a Reddit instance based off the provided client ID and
    secret.
    """
    return praw.Reddit(client_id=client_id, client_secret=client_secret,
                       user_agent="RedditFeed (by /u/jacobmstein)")


def stream_submissions(subreddit, webhook):
    """Streams new submissions on the provided subreddit to Slack."""
    start_time = time.time()
    try:
        for submission in subreddit.stream.submissions():
            if submission.created_utc < start_time:
                continue

            post_submission(submission, webhook)
    except ResponseException as e:
        code = e.response.status_code
        if 400 <= code < 500:
            print(f"Error, {code} received. Check your credentials then"
                  " try again.")
            sys.exit()

        print(f"Error, {code} received. Retrying in"
              " 5 seconds.")
        time.sleep(5)
        stream_submissions(subreddit, webhook)


def post_submission(submission, webhook):
    """Formats the provided submission and posts it to Slack."""
    message = {
        "attachments": [
            {
                "author_link":
                    f"https://reddit.com/u/{submission.author.name}",
                "author_name": f"/u/{submission.author.name}",
                "color": "#ff5700",
                "footer": f"/r/{submission.subreddit.display_name}",
                "image_url": submission.url,
                "text": submission.selftext,
                "title": submission.title,
                "title_link": submission.shortlink
            }
        ]
    }

    requests.post(webhook, json=message)


if __name__ == "__main__":
    config = get_config()
    reddit = get_reddit(config["clientId"], config["clientSecret"])
    stream_submissions(reddit.subreddit(config["subreddit"]),
                       config["webhook"])
