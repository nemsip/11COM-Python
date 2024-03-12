import pygame
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Set up the sound system
pygame.mixer.init()

# Define some constants
FPS = 44100
duration = 0.5  # Duration of each note in seconds
channels = 2  # Stereo

# Define some frequencies for different notes
C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00
A = 440.00
B = 493.88

# Define a dictionary to map notes to frequencies
notes = {
    'C': C,
    'D': D,
    'E': E,
    'F': F,
    'G': G,
    'A': A,
    'B': B
}

# Function to generate a waveform for a given frequency (using a saw wave)
def generate_wave(frequency, duration):
    num_samples = int(duration * FPS)
    amplitude = 2 ** 15 - 1
    waveform = np.array([[amplitude * (2 * (t * frequency / FPS - np.floor(0.5 + t * frequency / FPS))) for _ in range(channels)] for t in range(num_samples)])
    return waveform.astype(np.int16)

# Function to play a note
def play_note(note):
    frequency = notes.get(note.upper(), 0)  # Get the frequency of the note
    if frequency == 0:
        print("Invalid note")
        return

    sound = pygame.sndarray.make_sound(generate_wave(frequency, duration))
    sound.play()
    time.sleep(duration)

# Function to play a sequence of notes
def play_music(music_notes):
    for note in music_notes:
        if note != 'X':
            play_note(note)
        else:
            # If there's a space, wait for a short duration
            time.sleep(duration)

if __name__ == "__main__":
    # Example melody (Twinkle Twinkle Little Star)
    melody = "C C G G A A G X F F E E D D C"
    play_music(melody.split())
