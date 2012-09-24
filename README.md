# Rdio mass sync
Sync your entire collection to your mobile device for offline use

# Installation

## Get an Rdio API Key
If you don't already have an Rdio account, go [sign up](http://www.rdio.com/signup/).

You 'll now need an Rdio API key:

1. [Register for an Rdio API account](http://developer.rdio.com/member/register)
1. Click the link in the confirmation email to confirm your developer account
1. On the page that pops up, click the **Apply for access to use the API** link. 
1. On the *Rdio Application Registration* page:
 1. For **Name of your application**, enter `rdio-mass-sync`
 1. Make sure **Issue a new key for rdio API** is *checked*
 1. Make sure **I agree to the terms of service** is *checked*
 1. Click **Register Application**
1. The next page will show your API *Key* and *Shared Secret*. Make a note of these, you'll need them later.

## Install Rdio Mass Sync
Rdio Mass Sync add-on is available from the [GitHub](https://github.com/johnzimmerman/rdio-mass-sync).

If you're familliar with GitHub, you can [clone the repository](https://github.com/johnzimmerman/rdio-mass-sync). Otherwise, just download and unpack the [latest version](https://github.com/johnzimmerman/rdio-mass-sync/zipball/master).

## Configure Rdio Mass Sync
1. Open `rdio_consumer_credentials.py` in your favorite text editor
1. Add your Rdio Key and Secret to the `RDIO_CONSUMER_KEY` and `RDIO_CONSUMER_SECRET` variables

## Run all the things
1. `python mass_sync.py`
1. You'll be presented with an Rdio URL
1. Copy and paste the URL into your browser.
1. On the page that pops up, click **Allow**
1. Copy and paste the PIN code back into mass sync
1. When the request has been sent, open Rdio.com and verify the sync status of your collection.

# Credits
Thanks to [Charles Blaxland](https://github.com/ampedandwired) for a starting point for [this README](https://github.com/ampedandwired/rdio-xbmc/wiki).
