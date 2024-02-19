import os
from googleapiclient.discovery import build
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from moviepy.editor import VideoFileClip
def download_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
#video_url = input("Youtube video to download: ")
#download_video(video_url, r'C:\Users\robot\Videos\downloaded youtube videos')
def get_youtube_url(api_key, search_query, max_results=1):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        q=search_query,
        part='id',
        maxResults=max_results,
        type='video'
    )

    response = request.execute()

    if 'items' in response:
        video_id = response['items'][0]['id']['videoId']
        return f'https://www.youtube.com/watch?v={video_id}'
    else:
        return None

# Set up credentials
client_id = 'ENTER CLIENT ID'
client_secret = 'ENTER CLIENT SECRET'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


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
def returnSongsInPlaylist(user_id,playlist_number=0):
    user_id = user_id
    songs=[]
    # Check if there are playlists
    if playlists['items']:
        # Get the first playlist
        playlist_id = playlists['items'][playlist_number]['id']
        #songs.append( playlists['items'][playlist_number]['name'])

        # Get tracks from the first playlist
        results = sp.user_playlist_tracks(user_id, playlist_id=playlist_id)
        
        # Check if there are tracks
        if results['items']:
            # Print names of each track
            print("Tracks in the first playlist:")
            for item in results['items']:
                track_name = item['track']['name']
                songs.append(track_name)
                #print(track_name)
        else:
            print("No tracks found in the first playlist.")
    else:
        print("No playlists found for the user.")
    #print (f"Songs in Playlist:{songs}")
    return songs
def MP4ToMP3(video_path,output_audio_path):

    video = VideoFileClip(video_path)

    # Extract audio from video
    video.audio.write_audiofile(output_audio_path, codec="mp3")


spotify_api_key = 'ENTER SPOTIFY API KEY'
playlist_number=1
songs= returnSongsInPlaylist("sacb1q95pwg6ustbb157bspod", playlist_number)
playlist_title=playlists['items'][playlist_number]['name']

print(f"Songs in {playlist_title}: {songs}")
for song in songs:
    search_query = song
    print(f'Searching for {song} URL')
    youtube_url = get_youtube_url(spotify_api_key, search_query)
    #youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'      #for testing when exceed api limit

    if youtube_url:
        print(f"Found YouTube URL: {youtube_url}")
        download_video(youtube_url, f'C:\\Users\\robot\\Videos\\downloaded youtube videos\\{playlist_title}')
        VIDEO_FILE_PATH = f'C:\\Users\\robot\\Videos\\downloaded youtube videos\\{playlist_title}'
        AUDIO_FILE_PATH = f'C:\\Users\\robot\\Videos\\downloaded youtube videos\\{playlist_title}'
        #MP4ToMP3(VIDEO_FILE_PATH,AUDIO_FILE_PATH)

    else:
        print("No matching video found.")
    
