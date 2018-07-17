# RedditFeed
Reddit bot to stream submissions to a Slack channel.

## Installation
1. Verify you have [Python 3.6+](https://www.python.org/downloads/) installed.
2. Clone (`git clone https://github.com/jacobmstein/RedditFeed.git`) or [download](https://github.com/jacobmstein/RedditFeed/archive/master.zip) this repository.
3. [Create a Reddit application](https://ssl.reddit.com/prefs/apps/) and retrieve your client ID and secret.
4. [Create a Slack application](https://api.slack.com/apps/new) and create an incoming webhook.
5. Open `config.json` in your preferred text editor and set your client ID, secret, and webhook.
6. Install the necessary packages using pip, `pip install -r requirements.txt`.
7. Run the bot using `python bot.py`. (If Python 3.6+ isn't your default version of Python you may have to run `python3.6 bot.py` or something similar.)
