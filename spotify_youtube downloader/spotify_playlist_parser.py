import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up credentials
client_id = '41a21391e2484687b3e0f6a2060f6174'
client_secret = 'edf40ec8efc04e468be3c1535b6560e9'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# You can your Spotify USER ID from your Spotify account 
# (not your developer account)
playlists = sp.user_playlists('sacb1q95pwg6ustbb157bspod') 
user_id="sacb1q95pwg6ustbb157bspod"
def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("s   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

"""
for playlist in playlists['items']:
    print(playlist['name'])
    results = sp.user_playlist('sacb1q95pwg6ustbb157bspod', playlist['id'], fields="tracks,next")
    #print(results)
    tracks = results['tracks']
    show_tracks(tracks)
"""
def readEncodedData(user_id):
    # Replace 'sacb1q95pwg6ustbb157bspod' with your Spotify USER ID
    user_id = user_id
    encoded_Data=[]
    # Check if there are playlists
    if playlists['items']:
        # Get the first playlist
        first_playlist_id = playlists['items'][0]['id']
        
        # Get tracks from the first playlist
        results = sp.user_playlist_tracks(user_id, playlist_id=first_playlist_id)
        
        # Check if there are tracks
        if results['items']:
            # Print names of each track
            print("Tracks in the first playlist:")
            for item in results['items']:
                track_name = item['track']['name']
                encoded_Data.append(track_name +" ")
                print(track_name)
        else:
            print("No tracks found in the first playlist.")
    else:
        print("No playlists found for the user.")
    print (f"Encoded Data:{encoded_Data}")
    return encoded_Data

encoded= readEncodedData("sacb1q95pwg6ustbb157bspod")
print(f"Encoded {encoded}")
for song in encoded:
    #print(song)
    print(song[0], end="")



