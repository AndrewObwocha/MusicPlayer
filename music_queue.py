# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 5 - Music Queue
#
# ~ Created by CMPUT 175 Team ~
# =================================================================

# Install ytmusicapi using pip or pip3
from ytmusicapi import YTMusic
from structures import MusicQueue, Song, time_to_seconds
import os

NO_OF_RESULTS = 5

def clear():
    """
    Input: None
    Returns: None
    Working:
    This function clears terminal screen
    """
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

def extract_artists(song_info):
    """
    Input: Data of the song as originally retrieved (dictionary format)
    Returns: All artists involved in the song as a string or "NA" if no artist info is available.
    Working:
    This function makes sure that all artists involved in a song show up in the final 
    representation.
    """
    # Extract artist names from song_info['artists'] and store them in a list
    artists_data = [artist["name"] for artist in song_info['artists']]

    # Return NA if there is no artist information available
    if not artists_data:
        return 'NA'
    
    return ', '.join(artists_data) # String formatting artist info


def song_search(query):
    """
    Input: Search query
    Returns: Top 5 results from the retrieved data
    Working:
    This function invokes the search method on YTMusic object with required arguments
    and returns the top "NO_OF_RESULTS" results.
    """
    ytmusic = YTMusic()  # API insance

    # Use search API method and filter by top 'NO_OF_RESULTS' songs
    return ytmusic.search(query, filter="songs")[:NO_OF_RESULTS]

def filter_info(results):
    """
    Input: Search results in a JSON like format
    Returns: List of Song Objects
    Working:
    This function is supposed to extract the required information from the JSON,
    create Song objects and append them to a list. If an error occurs, raise an
    exception.
    """    
    songs = []  # Stores Song() objects

    # Creating a Song() object for each song returned from the API call
    for song in results:
        title = song["title"]
        artists = extract_artists(song)
        # Excepion handling for unanticipated time formats
        try:
            duration = time_to_seconds(song["duration"])
        except ValueError:
            raise ValueError("Invalid time format")
        else:
            songs.append(Song(title, artists, duration))
    
    return songs


def print_song_results(results):
    """
    Input: List containing "Song" objects
    Returns: None
    Working:
    This function is reponsible for printing the song results with a serial number beside them.
    """
    assert type(results[0]) == Song, "The list to be printed doesn't have the items of type 'Song'"

    print("RESULTS:")
    for i in range(len(results)):
        print(f"{i+1}. {results[i]}")

def search():
    """
    Input: None
    Return: A Song object representing the song the user wants to add into the Queue, or None if the user wants to go back
    Working:
    1. This function takes search query from the user
    2. Searches for the song using songSearch function
    3. Filters the information using filterInfo function
    4. Prints the song results using printSongResults function
    5. Asks for user choice
    6. Returns the chosen song information
    7. If the user wants to go back, it returns None
    """
    user_option = '0'
    while user_option == '0':
        clear()
        # Executing user query to return top songs based on their search
        user_query = input("Search: ")
        top_search_results = song_search(user_query)
        user_songs = filter_info(top_search_results)
        print_song_results(user_songs)

        # Menu for user to decide next action
        print("\nChoose one of the following options:")
        print("\tEnter a number (1-5) to add a song to the playlist")
        print("\tEnter '0' to search again")
        print("\tEnter 'q' to go back")
        
        # Input and input validation
        user_option = input(">> ")
        while user_option not in '012345q':
            print("Invalid Input")
            user_option = input(">> ")
        
        if user_option in '12345':
            return user_songs[int(user_option)-1]
        elif user_option == 'q':
            return
        

def main():
    """
    Drive Function
    """
    queue = MusicQueue()
    clear()
    print("WELCOME\n")
    choice_str = """Choose one of the following options:
                    \t1. Add Song
                    \t2. Next Song
                    \t3. Show Queue
                    \t4. Clear Queue
                    \t5. Quit
                    \tEnter the choice (eg: 2)
                """
    contBuild = True
    try:
        while contBuild:

            print('Currently playing:')
            if queue.is_empty() == False: 
                print('  ',queue.peek(),'\n')
            else: 
                print('  ',"None",'\n')

            print(choice_str)
            choice = input('>> ')
            while choice not in ['1','2','3','4','5']:
                print('Invalid Input.')
                choice = input('>> ')
            
            if choice == '1':
                song = search()
                if song != None:
                    if queue.is_empty():
                        queue.enqueue_b(song)
                    else:
                        place = input("Where would you like to add the song:\n\t1. Top\n\t2. End\n>> ")
                        while place not in ['1','2']:
                            print('Invalid Input.')
                            place = input('>> ')
                        
                        if place == '1':
                            queue.enqueue_f(song)
                        elif place == '2':
                            queue.enqueue_b(song)
                    print("Song added successfully!")
                    input("\nPress enter key to continue...")

            elif choice == '2':
                clear()
                queue.dequeue()
                print('Now playing:')
                if queue.size() > 0:
                    print("  ",queue.peek())
                else:
                    print("   None")
                input("\nPress enter key to continue...")

            elif choice == '3':
                clear()
                try:
                    print(queue)
                    input("\nPress enter key to continue...")
                except Exception as e:
                    print(e)
            
            elif choice == '4':
                clear()
                queue.clear()
                print('The queue has been cleared!')
                input("\nPress enter key to continue...")

            elif choice == '5':
                contBuild = False
            
            clear()

    except Exception as e:
        print(e)

    print("Thanks for listening!")

if __name__ == "__main__":
    main()