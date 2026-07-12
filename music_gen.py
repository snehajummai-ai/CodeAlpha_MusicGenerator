# Import required classes from music21
from music21 import stream, note


# Create a music stream
# Stream is used to store musical notes
melody = stream.Stream()


# List of musical notes
# These notes will form the melody
notes = ['C4', 'E4', 'G4', 'A4', 'G4', 'E4', 'C4']


# Loop through each note
for n in notes:

    # Create a musical note object
    music_note = note.Note(n)

    # Add the note to the melody stream
    melody.append(music_note)


# Save the melody as a MIDI file
melody.write('midi', 'output.mid')


# Print success message
print("Music file generated successfully: output.mid - music_gen.py:30")