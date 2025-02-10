from .base import Vector, Sine_Zeros
import numpy as np
import matplotlib.pyplot as plt
import live
from midiutil import MIDIFile


def generate_scale(M=7, root=0, N=12, theta=0):
    """
    Generate a musical scale using zero crossings of a sine wave.

    Parameters
    ----------
    M : int, optional
        Number of steps in the scale (default is 7).
    root : int, optional
        Root note of the scale (default is 0).
    N : int, optional
        Total number of notes (default is 12).
    theta : float, optional
        Phase shift for the scale generation (default is 0).

    Returns
    -------
    Vector
        A vector containing the generated scale.
    """
    repeat = 12
    root_shifted = root % N
    scale = (Sine_Zeros(M, N, theta=theta, repeat=repeat)
             .project(np.arange(repeat * N))
             .add(root_shifted - N)
             .clip()
             .astype(int))
    return scale


def generate_grid(N=16, repeat=4):
    """
    Generate a time grid for sequencing.

    Parameters
    ----------
    N : int, optional
        Number of time steps per repeat (default is 16).
    repeat : int, optional
        Number of repetitions (default is 4).

    Returns
    -------
    Vector
        A vector containing the generated time grid.
    """
    grid = Vector(np.arange(N * repeat)).astype(int)
    return grid


def create_clip(set, track_id, clip_id, length, erase=True):
    """
    Create or retrieve a MIDI clip in a specified track.

    Parameters
    ----------
    set : object
        The Live set object containing tracks and clips.
    track_id : int
        The index of the track where the clip will be created.
    clip_id : int
        The index of the clip slot in the track.
    length : float
        The length of the clip in beats.
    erase : bool, optional
        If True, removes existing notes from the clip before creation (default is True).

    Returns
    -------
    object
        The created or retrieved clip object.

    Raises
    ------
    ValueError
        If the specified track is not a MIDI track.
    """
    track = set.tracks[track_id]

    if not track.is_midi_track:
        raise ValueError("First track must be a MIDI track")

    clip = set.tracks[track_id].clips[clip_id]
    if clip is None:
        clip = track.create_clip(clip_id, length)
    else:
        if erase:
            clip.live.cmd("/live/clip/remove/notes",(track_id, clip_id))

    return clip


def save_to_midi(note_list, filename="output.mid", bpm=120):
    """
    Export a Sequence of Notes to a MIDI file using midiutil.

    Parameters
    ----------
    note_list : list of Note
        The list of notes to be exported.
    filename : str, optional
        The name of the output MIDI file (default is "output.mid").
    bpm : int, optional
        The tempo of the MIDI file in beats per minute (default is 120 BPM).
    """
    midi = MIDIFile(1)
    midi.addTempo(track=0, time=0, tempo=bpm)
    
    for note in note_list:
        pitch = note.pitch
        velocity = note.velocity
        start_time = note.start_time  # Time in beats
        duration = note.duration  # Duration in beats

        # Add note to MIDI track (channel=0, track=0)
        midi.addNote(track=0, channel=0, pitch=pitch, time=start_time, 
                    duration=duration, volume=velocity)

    # Save to file
    with open(filename, "wb") as f:
        midi.writeFile(f)

    print(f"MIDI file saved as {filename}")

