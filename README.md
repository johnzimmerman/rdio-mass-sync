# Rdio mass sync
Sync your entire music collection to your mobile device for offline use

## Prerequisites

### Get a Rdio account
If you don't already have a Rdio account, sign up [here](http://www.rdio.com/signup/).

### Next, sign up for a Rdio developer account
1. [Register for a Rdio API account](http://developer.rdio.com/member/register)
2. Click the link in the confirmation email to confirm your developer account
3. On the page that pops up, click the **Apply for access to use the API** link
4. On the *Rdio Application Registration* page:
 1. For **Name of your application**, enter `rdio-mass-sync`
 2. Make sure **Issue a new key for rdio API** is checked
 3. Make sure **I agree to the terms of service** is checked
 4. Click **Register Application**
5. The next page will show your API Key and Shared Secret. Make a note of these, you'll need them later.

## Install Rdio mass sync
You can either [clone the repository](https://github.com/johnzimmerman/rdio-mass-sync) or download and unpack the [latest version](https://github.com/johnzimmerman/rdio-mass-sync/zipball/master).

## Configure Rdio mass sync
1. Open `rdio_consumer_credentials.py` in your favorite text editor
2. Add your Rdio Key and Secret to the `RDIO_CONSUMER_KEY` and `RDIO_CONSUMER_SECRET` variables

## Run all the things
1. `python mass_sync.py`
2. You'll be presented with a Rdio URL
3. Copy and paste the URL into your browser.
4. On the page that pops up, click **Allow**
5. Copy and paste the PIN back into Rdio mass sync
6. When the request has been sent, open Rdio on your mobile device to verify the sync progress of your collection. Your phone's sync progress is viewable within the Rdio app's Settings menu.