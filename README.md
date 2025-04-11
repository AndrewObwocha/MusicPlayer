# Music Queue CLI Application

## Description

This is a command-line interface (CLI) application written in Python that allows users to search for songs on YouTube Music, add them to a queue, and manage that queue. It simulates a music playback queue where you can see the total duration, add songs to the front or back, and advance to the next song.

This project utilizes the `ytmusicapi` library to interact with YouTube Music for searching songs.

## Features

*   **Search Songs:** Find songs on YouTube Music using a search query.
*   **View Search Results:** Displays the top 5 song results matching the query.
*   **Add to Queue:**
    *   Add selected songs to the *back* of the queue (standard enqueue).
    *   Add selected songs to the *front* of the queue (priority enqueue).
*   **View Queue:** Display the current list of songs in the queue, including the total number of songs and the total duration.
*   **See Current Song:** Shows the song currently at the front of the queue (the "now playing" song).
*   **Next Song:** Removes the current song from the front of the queue (simulates playing it and moving to the next).
*   **Clear Queue:** Empties the entire music queue.
*   **User-Friendly Interface:** Simple menu-driven interaction.

## Requirements

*   Python 3.x
*   `ytmusicapi` library

## Installation & Setup

1.  **Clone the repository or download the files:**
    Make sure you have both `music_queue.py` and `structures.py` in the same directory.

2.  **Install the required library:**
    Open your terminal or command prompt and run:
    ```bash
    pip install ytmusicapi
    # or pip3 install ytmusicapi
    ```

## How to Use

1.  **Navigate to the directory** containing the files in your terminal.

2.  **Run the application:**
    ```bash
    python music_queue.py
    # or use python3 if needed
    # python3 music_queue.py
    ```

3.  **Follow the on-screen prompts:**
    *   You will be presented with a main menu:
        *   `1. Add Song`: Initiates the search process.
            *   Enter your search query.
            *   Choose a song (1-5) from the results to add.
            *   Select whether to add it to the `Top` (front) or `End` (back) of the queue.
            *   Enter `0` to search again, or `q` to go back to the main menu without adding.
        *   `2. Next Song`: Removes the song at the front of the queue.
        *   `3. Show Queue`: Displays the current queue details.
        *   `4. Clear Queue`: Removes all songs from the queue.
        *   `5. Quit`: Exits the application.

## File Structure

*   `music_queue.py`: Contains the main application logic, user interface interactions, and calls to the YouTube Music API.
*   `structures.py`: Defines the `Song` class (representing a single song) and the `MusicQueue` class (the queue data structure itself), along with helper functions for time conversion.

---
