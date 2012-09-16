from urllib2 import HTTPError

from rdio import Rdio
from rdio_consumer_credentials import *


rdio = Rdio((RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET))
keys = []

try:
  # authenticate against the Rdio service
  url = rdio.begin_authentication('oob')
  print "Go to: " + url
  verifier = raw_input("Then enter the code: ").strip()
  rdio.complete_authentication(verifier)

  # get tracks in collection
  tracks = rdio.call('getTracksInCollection', {'sort': 'artist'})
  if (tracks['status'] == 'ok'):
    for track in tracks['result']:
      # add keys to a list
      keys.append(track['key'])
  else:
    print "ERROR: " + tracks['message']

  # create a comma separated string
  keys_string = ",".join(keys)
  print "Sending request to Rdio"
  rdio.call('setAvailableOffline', {'keys': keys_string, 'offline': True})
  print "Request sent. Open your Rdio mobile app to check the syncing status."

except HTTPError, e:
  # if we have a protocol error, print it
  print e.read()