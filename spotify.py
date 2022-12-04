
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import csv

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="bd74c8c910954fc09415cfea94d13a26",
                                                        client_secret="b3ce6caec2904c009dac6e776ff49bd1"))                        
song_dict = {'sadness' : [],'joy' : [],'anger' : [],'love' : [], 'surprise' : [],'fear' : [] }
song_csv = []
playlists = {
            'sadness' : ["https://open.spotify.com/playlist/3c0Nv5CY6TIaRszlTZbUFk",
                    "https://open.spotify.com/playlist/70VaOHyjpsWcmA4gxosExZ"],

            'joy' : ["https://open.spotify.com/playlist/1h90L3LP8kAJ7KGjCV2Xfd",
                    "https://open.spotify.com/playlist/4AnAUkQNrLKlJCInZGSXRO"],

            'anger' : ["https://open.spotify.com/playlist/5O12S9z3O8dEhHWt3bPbxm",
                        "https://open.spotify.com/playlist/23lYtJMh8NWBahDc4FX8Ee"],

            'love' : ["https://open.spotify.com/playlist/6oNsYDhN95gkENsdFcAwTh",
                        "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn"],

            'surprise' : ["https://open.spotify.com/playlist/4o5SxWNsTNLOi9ahHeJF8A"],
            
            'fear' : ["https://open.spotify.com/playlist/5SJpZzc6nhaezmRDFOm3Bt",
                        "https://open.spotify.com/playlist/6VcH2xJR5uvi8NJ1YlUO74"]                    
            }

def convert(ms):
    s  = "%02d" % (int(ms/1000)%60)
    m  = "%02d" % (int(ms/(1000*60))%60)
    return ("00:"+str(m)+":"+str(s))

for emo, links in playlists.items():
    for i in links:
        id = i.split("/")[4]
        emo_playlist = sp.user_playlist_tracks(playlist_id=id)
        track = emo_playlist['items']
        for song in track :
            artist= song['track']['artists'][0]['name']
            artist_id = song['track']['artists'][0]['id']
            name = song['track']['name']
            url = song['track']['external_urls']['spotify']
            song_id = song["track"]["id"]
            duration = convert(int(song['track']['duration_ms']))
            popularity = song['track']['popularity']

            temp = [artist,artist_id,name,song_id,emo,duration,popularity,url]
            song_csv.append(temp)

"""
header = ['artist','artist_id','name','song_id','emo','duration','popularity','url']
with open('song.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for song in song_csv:
       # print(type(song))
        writer.writerow(song)

f.close()
"""