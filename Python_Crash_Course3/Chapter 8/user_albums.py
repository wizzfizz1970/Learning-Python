'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.'''



def make_album(artist_name, album_title, num_tracks=None):
    """Build a dictionary describing a music album."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if num_tracks:  # Add the number of tracks if provided
        album['tracks'] = num_tracks
    return album

# Prompt the user to input album details
print("Enter album details. Type 'quit' at any time to stop.")

while True:
    # Get user input for artist name
    artist = input("\nEnter artist name: ")
    if artist.lower() == 'quit':
        break

    # Get user input for album title
    title = input("Enter album title: ")
    if title.lower() == 'quit':
        break

    # Get user input for number of tracks (optional)
    tracks = input("Enter the number of tracks (optional, or type 'skip'): ")
    if tracks.lower() == 'quit':
        break
    if tracks.lower() == 'skip':
        tracks = None
    else:
        tracks = int(tracks) if tracks.isdigit() else None

    # Create the album dictionary and display it
    album = make_album(artist, title, tracks)
    print("\nAlbum details:", album)

print("\nThank you for using the album maker!")

