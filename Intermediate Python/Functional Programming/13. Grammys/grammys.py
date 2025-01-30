# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
    return song[1] > 5.00

def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    sec = (duration - minutes) * 100
    
    return minutes*60+round(sec)

from functools import reduce
def add_durations(total_duration, song):
    return total_duration + song[1]


long_songs = filter(longer_than_five_minutes, playlist)
convert = map(minutes_to_seconds, playlist)
total_duration = reduce(add_durations, playlist, 0)

print(list(long_songs))
print(list(convert))
print(total_duration)