from .base import Vector
import numpy as np


class Note:
    """
    A class representing a musical note.

    Attributes
    ----------
    pitch : int
        The pitch of the note.
    velocity : int
        The velocity (intensity) of the note.
    start_time : float
        The start time of the note.
    duration : float
        The duration of the note.
    """
    def __init__(self, pitch, velocity, start_time, duration, mute=False):
        """
        Initialize a Note instance.

        Parameters
        ----------
        pitch : int
            The pitch value of the note.
        velocity : int
            The velocity (intensity) of the note.
        start_time : float
            The start time of the note.
        duration : float
            The duration of the note.
        """
        self.pitch = int(pitch)
        self.start_time = start_time
        self.velocity = int(velocity)
        self.duration = duration
        self.mute = mute

    def __repr__(self):
        """
        Return a string representation of the Note.
        """
        return f"pitch:{self.pitch}, start_time:{self.start_time}, duration:{self.duration}, velocity:{self.velocity}"

    def tolist(self):
        """
        Convert the note to a list format.

        Returns
        -------
        list
            A list containing pitch, start_time, duration, velocity, and a mute flag.
        """
        return [self.pitch, self.start_time, self.duration, self.velocity, self.mute]


class Sequence:
    """
    A class representing a sequence of musical notes.
    
    Attributes
    ----------
    note_list : list of Note
        A list containing Note objects.
    """
    def __init__(self, start_time_vector, pitch_vector, velocity_vector=None, duration_vector=None):
        """
        Initialize a Sequence of notes.

        Parameters
        ----------
        start_time_vector : Vector
            A vector containing the start times of the notes.
        pitch_vector : Vector
            A vector containing the pitch values of the notes.
        velocity_vector : Vector, optional
            A vector containing the velocity values (default is 100 for all notes).
        duration_vector : Vector, optional
            A vector containing the duration values (default is 0.5 for all notes).
        """
        M = len(start_time_vector)

        pitch_vector.resize(M).astype(int)

        if velocity_vector is None:
            velocity_vector = Vector(100)
        velocity_vector = velocity_vector.resize(M).astype(int)
    
        if duration_vector is None:
            duration_vector = Vector(0.5)

        duration_vector = duration_vector.resize(M)

        note_list = []
        for m in range(M):
            start_time = start_time_vector[m]
            pitch = pitch_vector[m]
            velocity = velocity_vector[m]
            duration = duration_vector[m]
            note_temp = Note(pitch, velocity, start_time, duration)
            note_list.append(note_temp)

        self.note_list = note_list

    def reset(self):
        """
        Reset the sequence by clearing all notes.
        """
        self.note_list = []

    def __iter__(self):
        """
        Allow iteration over notes in the sequence.

        Returns
        -------
        iterator
            An iterator over the notes in the sequence.
        """
        return iter(self.note_list)

    def get_notes(self):
        """
        Send list of notes
        """
        return self.note_list


    def send_to_ableton(self, clip, length=16):
        """
        Send sequence to ableton clip
        """
        for note in self.note_list:   
            clip.add_note(note.pitch, note.start_time, note.duration, note.velocity, note.mute)

        return None
