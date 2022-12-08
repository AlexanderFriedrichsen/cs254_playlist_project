# import json
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans

# # load json files
# json_files = []
# for i in range(0, 999):
#     print("file #" + str(i))
#     num1 = i*1000
#     num2 = num1+999
#     new_str = str(num1) + "-" + str(num2)
#     with open('data\spotify_million_playlist_dataset\data\mpd.slice.{}.json'.format(new_str)) as f:
#         json_files.append(json.load(f))
        
        
        
import json
import numpy as np
from sklearn.cluster import KMeans
import os
import collections

def feature_extractor(data):
    # Extract the average tempo, danceability, and energy of the songs in the playlist
    tempos = [song['tempo'] for song in data['playlist']['tracks']]
    danceabilities = [song['danceability'] for song in data['songs']]
    energies = [song['energy'] for song in data['songs']]
    avg_tempo = np.mean(tempos)
    avg_danceability = np.mean(danceabilities)
    avg_energy = np.mean(energies)
    
    # Extract the most common artist and genre in the playlist
    artists = [song['artist'] for song in data['songs']]
    genres = [song['genre'] for song in data['songs']]
    most_common_artist = collections.Counter(artists).most_common(1)[0]
    most_common_genre = collections.Counter(genres).most_common(1)[0]
    
    # Return the extracted features as a list
    return [avg_tempo, avg_danceability, avg_energy, most_common_artist, most_common_genre]



i = 0
# Load the playlist data from the json files
playlist_data = []
for file in os.listdir('data\spotify_million_playlist_dataset\data'):
    if (i < 20):
        print(file)
        with open('data\spotify_million_playlist_dataset\data\{}'.format(file)) as f:
            data = json.load(f)
            playlist_data.append(data)
    i += 1
    
X = np.array([feature_extractor(d) for d in playlist_data])

# # Perform k-means clustering on the data
# kmeans = KMeans(n_clusters=20)
# kmeans.fit(X)

# # Get the cluster that the user's input string belongs to
# def get_cluster_for_string(string):
#     features = feature_extractor(string)
#     cluster_idx = kmeans.predict([features])
#     return cluster_idx

# # Create a new playlist based on the cluster of the user's input
# def create_playlist_from_string(string):
#     cluster_idx = get_cluster_for_string(string)
#     playlist = []
#     for i, data in enumerate(playlist_data):
#         if kmeans.labels_[i] == cluster_idx:
#             playlist.append(data)
#     return playlist