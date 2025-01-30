liked_songs = {
    'Waste': 'Brockhampton',
    'Daylily': 'Movements',
    'Rain': 'Sleep Token'
}

def write_liked_songs_to_file(songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artist in songs.items():
            file.write(f'{song} by {artist}\n')
    print(f"Successfully added Like songs to {file_name}")
    
    
write_liked_songs_to_file(liked_songs, 'Intermediate Python/File Input Output/07. The File Realm/music.txt')