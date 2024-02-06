
import random

# Created a class called Music Player
class Music_Player:
    # Created a constructor
    def __init__(self):
        self.audio = []
        self.ratings = []
        return
    
    # Method to create audio using URL
    def create_audio(self, url):
        return url
    
    # Method to create playlist by genre
    def create_playlist(self, genre):
        return genre
    
    # Method to search audio by name
    def search_audio(self, url, name):
        return url
    
    # Method to search playlist by name
    def search_playlist(self, url, name):
        return url
    
    # Method to add audio to the list of audio
    def add_audio(self, audio):
        self.audio.append(audio)
    
    # Method to rate audio
    def rate_audio(self, audio, rating):
        self.rate(rating)
    
    # Method to rate playlist
    def rate_playlist(self, playlist, rating):
        self.rate(rating)

    # Method to add rating into rating list
    def rate(self, rating):
        self.ratings.append(rating)
    
    # Method to calculate average rating of audio
    def calculate_average_rating_audio(self):
        sum = 0
        for data in self.ratings:
            sum = sum + data
        length_rating = len(self.ratings)
        average_rating = sum/length_rating
        return average_rating
    
    # Method to calculate average rating of playlist
    def calculate_average_rating_playlist(self):
        sum = 0
        for data in self.ratings:
            sum = sum + data
        length_rating = len(self.ratings)
        average_rating = sum/length_rating
        return average_rating

    # Defining methods for audio player customization. We can call the methods as needed.
    # For example, we can call play method to play audio, pause method for pause audio
    # Rewind method to rewind audio and forward method to forward audio
    def customize(self):
        print("Customized audio player features applied.")
    
    def play(self):
        self.playing = True
        print("Audio is playing.")
    
    def pause(self):
        self.playing = False
        print("Audio is paused.")
    
    def rewind(self):
        print("Rewinding audio.")
    
    def forward(self):
        print("Forwarding audio.")
    
    
# Main method execution
if __name__ == "__main__":
    # Created 3 objects for class Music Player to access attributes
    user_1 = Music_Player()
    user_2 = Music_Player()
    user_3 = Music_Player()

# Method to generate random rating to give random rating to audio and playlist
def generate_random_rating():
        return random.randint(1, 5)

# Created audio using URLs available online and store it in respective variables
audio1 = user_1.create_audio("https://open.spotify.com/playlist/37i9dQZF1DXa2huSXaKVkW")
audio2 = user_2.create_audio("https://open.spotify.com/playlist/37i9dQZF1DXd8cOUiye1o2")
audio3 = user_3.create_audio("https://open.spotify.com/playlist/37i9dQZF1DWXtlo6ENS92N")

# Created multiple playlists based on genre of the song
playlist1 = user_1.create_playlist("Rock")
playlist2 = user_2.create_playlist("Jazz")
playlist3 = user_3.create_playlist("Melody")

# Added audio files to playlists
user_1.add_audio(audio1)
user_2.add_audio(audio2)
user_3.add_audio(audio3)

# Random ratings to each audio
user_1.rate_audio(audio1, generate_random_rating())
user_2.rate_audio(audio2, generate_random_rating())
user_3.rate_audio(audio3, generate_random_rating())

# Random ratings to each playlist
user_1.rate_playlist(playlist1, generate_random_rating())
user_2.rate_playlist(playlist2, generate_random_rating())
user_3.rate_playlist(playlist3, generate_random_rating())

# Print an empty line
print()

# Print average ratings for both audio and Playlist
print("Average rating for Audio-1: ", user_1.calculate_average_rating_audio())
print("Average rating for Playlist-2: ", user_2.calculate_average_rating_playlist())

# Print an empty line
print()

# Print the URL of song by name search
print("URL of song 'Harleys in Hawaii' is: ", user_1.search_audio("https://open.spotify.com/track/5nCthAh3jt4xKuLJAifAaR","Harleys In Hawaii"))
print("URL of song 'A Thousand Years' is: ", user_1.search_audio("https://open.spotify.com/track/6z5Yh7kOKeLjqIsNdokIpU","Thousand Years"))
print("URL of song 'Perfect By Ed Sheeran' is: ", user_1.search_audio("https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v","Perfect"))

print()

# Print the URL of playlist by name search
print("URL of playlist 'Dinner Time' is: ", user_2.search_playlist("https://open.spotify.com/playlist/37i9dQZF1DX4xuWVBs4FgJ","DinnerTime"))
print("URL of playlist 'Jazz Time' is: ", user_2.search_playlist("https://open.spotify.com/playlist/37i9dQZF1DWWKeNBqaIy5U","JazzTime"))
print("URL of playlist 'Lounge Dinner' is: ", user_2.search_playlist("https://open.spotify.com/playlist/37i9dQZF1DX6kz6Kli3wib","LoungeDinner"))

print()

# Calling the customized methods
user_1.customize()
print()

# Audio player control, calling all customized methods
user_1.play()
user_1.pause()
user_1.rewind()
user_1.forward()