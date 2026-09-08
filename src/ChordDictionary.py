class ChordDictionary:
    """MIDI notes for common chord symbols used by DEMH inputs."""

    _ROOTS = {
        "C": 0,
        "C#": 1,
        "Db": 1,
        "D": 2,
        "D#": 3,
        "Eb": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "Gb": 6,
        "G": 7,
        "G#": 8,
        "Ab": 8,
        "A": 9,
        "A#": 10,
        "Bb": 10,
        "B": 11,
    }

    _QUALITIES = {
        "": (0, 4, 7),
        "m": (0, 3, 7),
        "dim": (0, 3, 6),
        "aug": (0, 4, 8),
        "sus2": (0, 2, 7),
        "sus4": (0, 5, 7),
        "6": (0, 4, 7, 9),
        "m6": (0, 3, 7, 9),
        "7": (0, 4, 7, 10),
        "maj7": (0, 4, 7, 11),
        "m7": (0, 3, 7, 10),
        "m7b5": (0, 3, 6, 10),
        "dim7": (0, 3, 6, 9),
        "aug7": (0, 4, 8, 10),
        "7b5": (0, 4, 6, 10),
        "7#5": (0, 4, 8, 10),
        "7sus4": (0, 5, 7, 10),
        "add9": (0, 4, 7, 14),
        "madd9": (0, 3, 7, 14),
        "9": (0, 4, 7, 10, 14),
        "maj9": (0, 4, 7, 11, 14),
        "m9": (0, 3, 7, 10, 14),
        "11": (0, 4, 7, 10, 14, 17),
        "m11": (0, 3, 7, 10, 14, 17),
        "13": (0, 4, 7, 10, 14, 17, 21),
        "maj13": (0, 4, 7, 11, 14, 17, 21),
        "m13": (0, 3, 7, 10, 14, 17, 21),
    }

    _ALIASES = {
        "M": "",
        "maj": "",
        "min": "m",
        "minor": "m",
        "M7": "maj7",
        "7M": "maj7",
        "maj7": "maj7",
        "min7": "m7",
        "-7": "m7",
        "-": "m",
        "°": "dim",
        "o": "dim",
        "+": "aug",
    }

    def __init__(self, octave=4):
        base_midi = 12 * (octave + 1)
        self.chord = {}

        for root_name, semitone in self._ROOTS.items():
            root_midi = base_midi + semitone
            for quality, intervals in self._QUALITIES.items():
                self.chord[root_name + quality] = [
                    root_midi + interval for interval in intervals
                ]

            for alias, quality in self._ALIASES.items():
                intervals = self._QUALITIES[quality]
                self.chord[root_name + alias] = [
                    root_midi + interval for interval in intervals
                ]