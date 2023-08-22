import os
import random
import pretty_midi


class ChordGenerator:
    def __init__(self):
        self.pitch_ranges = {
            "maj7": range(60, 73),
            "min7": range(58, 71),
            "dom7": range(57, 70),
            "min7b5": range(55, 68),
            "bIIImin7": range(56, 69),
            "bIIdom7": range(58, 71),
            "bVIdom7": range(54, 67),
        }

        # Add more pitch ranges for chord qualities and extensions as needed

    def generate_advanced_chord_progression(self):
        try:
            # Define chord qualities with possible extensions
            chord_definitions = [
                ("maj7", ["", "9", "maj7#11", "13"]),
                ("min7", ["", "9", "11", "b13"]),
                ("dom7", ["", "9", "11", "13"]),
                ("min7b5", ["", "b9", "11", "b13"]),
                ("bIIImin7", ["", "9", "11", "b13"]),
                ("bIIdom7", ["", "9", "11", "13"]),
                ("bVIdom7", ["", "9", "11", "13"]),
            ]

            # Define borrowed chord possibilities
            borrowed_chords = [
                ("bII", "dom7"),
                ("bIII", "min7"),
                ("bVI", "min7"),
            ]

            # Define the chord progression length
            progression_length = 8  # You can adjust this as needed

            # Initialize the chord progression list
            chord_progression = []

            # Generate the chord progression
            for _ in range(progression_length):
                # Choose a random chord definition
                chord_quality, chord_extensions = random.choice(chord_definitions)

                # Choose a random chord extension
                chord_extension = random.choice(chord_extensions)

                # Choose whether to introduce a borrowed chord
                use_borrowed_chord = random.choice([True, False])

                if use_borrowed_chord:
                    borrowed_chord_quality, borrowed_chord_extensions = random.choice(borrowed_chords)
                    chord = borrowed_chord_quality + borrowed_chord_extensions
                else:
                    chord = chord_quality + chord_extension

                chord_progression.append(chord)

            return chord_progression

        except Exception as ex:
            raise Exception("An error occurred during chord progression generation: " + str(ex))


# Usage example
try:
    chord_generator = ChordGenerator()
    progression = chord_generator.generate_advanced_chord_progression()
    print(progression)
except Exception as ex:
    print("An unexpected error occurred:", ex)


class MelodyGenerator:
    def generate_melody_with_variations(self, chord_progression):
        try:
            # Define pitch ranges for different chord qualities
            pitch_ranges = {
                "maj7": range(60, 73),
                "min7": range(58, 71),
                "dom7": range(57, 70),
                "min7b5": range(55, 68),
                "bIIImin7": range(56, 69),
                "bIIdom7": range(58, 71),
                "bVImin7": range(53, 66),
                "bVIdom7": range(54, 67),
                "min6": range(57, 70),
                "min11": range(58, 71),
                "dim7": range(51, 64),
                "aug7": range(60, 73)
                # Add more chord qualities and their corresponding pitch ranges here
            }

            default_pitch_range = range(40, 80)  # Choose an appropriate default pitch range

            # Initialize the melody list
            melody = []

            for chord in chord_progression:
                chord_quality = chord[:-2]  # Remove extension

                chord_notes = pitch_ranges.get(chord_quality, default_pitch_range)

                # Choose a random note from the chord notes
                melody_note = random.choice(chord_notes)

                # Handle cases where melody_note is out of range
                if melody_note < min(chord_notes):
                    melody_note = min(chord_notes)
                elif melody_note > max(chord_notes):
                    melody_note = max(chord_notes)

                # Introduce passing tone, neighbor tone, or suspension with probability
                variation_type = random.choice(["passing", "neighbor", "suspension"])
                if variation_type == "passing":
                    passing_note = random.choice(chord_notes)
                    melody.append([melody_note, passing_note, melody_note])
                elif variation_type == "neighbor":
                    neighbor_note = random.choice(chord_notes)
                    melody.append([melody_note, neighbor_note, melody_note])
                elif variation_type == "suspension":
                    suspension_note = melody_note - 1
                    melody.append([melody_note, suspension_note, melody_note])

            return melody

        except ValueError as ve:
            raise ValueError(f"Error during melody generation: {ve}")
        except Exception as ex:
            raise Exception(f"An unexpected error occurred during melody generation: {ex}")

class DynamicsGenerator:
    def apply_dynamics_and_articulation(self, melody):
        try:
            print("Melody:", melody)
            for phrase in melody:
                print("Phrase:", phrase)
                for i, event in enumerate(phrase):
                    if isinstance(event, dict):
                        dynamic = random.choice(["pp", "p", "mp", "mf", "f", "ff"])
                        event["dynamic"] = dynamic
                        # ...
        except Exception as ex:
            raise Exception("An error occurred during dynamics and articulation application: " + str(ex))

# Usage example
try:
    composition = [
        [{"note": 60, "duration": 0.5}, {"note": 62, "duration": 0.5}],
        [{"note": 63, "duration": 0.5}, {"note": 65, "duration": 0.5}]
    ]  # Sample melody composition
    dynamics_generator = DynamicsGenerator()
    composition_with_dynamics = dynamics_generator.apply_dynamics_and_articulation(composition)
    print(composition_with_dynamics)
except Exception as ex:
    print("An unexpected error occurred:", ex)

class PhrasingGenerator:
    def introduce_rhythmic_variation(self, melody):
        try:
            if melody is None:
                raise Exception("The melody is None. Please provide a valid melody.")

            # Define rhythmic patterns for different phrasing techniques
            phrasing_patterns = {
                "regular": [0.5, 0.5],
                "syncopated": [0.25, 0.75],
                "dotted": [0.75, 0.25],
                "swing": [0.375, 0.125, 0.375, 0.125]
            }

            # Apply rhythmic variation and phrasing to the melody
            for section in melody:
                if not isinstance(section, list):
                    raise Exception("Each section of the melody should be a list.")

                phrasing_technique = random.choice(list(phrasing_patterns.keys()))
                rhythmic_pattern = phrasing_patterns.get(phrasing_technique, [])

                for i, event in enumerate(section):
                    if isinstance(event, dict):
                        event["duration"] = rhythmic_pattern[i % len(rhythmic_pattern)]

            return melody

        except Exception as ex:
            raise Exception("An error occurred during rhythmic variation introduction: " + str(ex))

# Usage example
try:
    melody = [
        [{"note": 60, "duration": 0.5}, {"note": 62, "duration": 0.5}],
        [{"note": 63, "duration": 0.5}, {"note": 65, "duration": 0.5}]
    ]  # Sample melody with variations
    phrasing_generator = PhrasingGenerator()
    melody_with_phrasing = phrasing_generator.introduce_rhythmic_variation(melody)
    print(melody_with_phrasing)
except Exception as ex:
    print("An unexpected error occurred:", ex)

class CadenceGenerator:
    def generate_cadences_and_key_changes(self, chord_progression):
        try:
            # Define cadence probabilities
            cadence_probabilities = {
                "authentic": 0.4,
                "plagal": 0.2,
                "deceptive": 0.1
            }

            # Define possible key changes
            key_changes = ["C", "D", "E", "F", "G", "A", "B"]

            # Initialize the new chord progression list
            new_chord_progression = []

            for i, chord in enumerate(chord_progression):
                new_chord = chord

                # Introduce key change with probability
                if random.random() < cadence_probabilities.get("authentic", 0):
                    new_key = random.choice(key_changes)
                    new_chord = new_key + chord[1:]  # Change root of the chord
                    new_chord_progression.append(new_chord)

                # Apply other cadence types as needed
                # ...

                # If no key change or cadence, keep the original chord
                if new_chord == chord:
                    new_chord_progression.append(chord)

            return new_chord_progression

        except Exception as ex:
            raise Exception("An error occurred during cadence and key change generation: " + str(ex))


# Usage example
try:
    chord_progression = ["Cmaj7", "Dmin7", "G7", "Cmaj7"]  # Sample chord progression
    cadence_generator = CadenceGenerator()
    new_progression = cadence_generator.generate_cadences_and_key_changes(chord_progression)
    print(new_progression)
except Exception as ex:
    print("An unexpected error occurred:", ex)

class CounterpointGenerator:
    def generate_counterpoint_lines(self, melody):
        try:
            # Define possible intervals for counterpoint
            counterpoint_intervals = [-9, -7, -5, -4, -2, 2, 4, 5, 7, 9]

            # Initialize the counterpoint melody list
            counterpoint_melody = []

            for section in melody:
                counterpoint_section = []

                for event in section:
                    original_note = event["note"]
                    interval = random.choice(counterpoint_intervals)
                    counterpoint_note = original_note + interval

                    # Ensure the counterpoint note is within a reasonable pitch range
                    counterpoint_note = max(min(counterpoint_note, 88), 24)  # MIDI note values

                    counterpoint_event = {
                        "note": counterpoint_note,
                        "duration": event["duration"],
                        "dynamic": event["dynamic"],
                        "articulation": event["articulation"]
                    }
                    counterpoint_section.append(counterpoint_event)

                counterpoint_melody.append(counterpoint_section)

            return counterpoint_melody

        except Exception as ex:
            raise Exception("An error occurred during counterpoint generation: " + str(ex))


# Usage example
try:
    melody = [
        [{"note": 60, "duration": 0.5, "dynamic": "mf", "articulation": "legato"},
         {"note": 62, "duration": 0.5, "dynamic": "mf", "articulation": "legato"}],
        [{"note": 63, "duration": 0.5, "dynamic": "f", "articulation": "staccato"},
         {"note": 65, "duration": 0.5, "dynamic": "f", "articulation": "staccato"}]
    ]  # Sample melody with variations and dynamics
    counterpoint_generator = CounterpointGenerator()
    counterpoint_melody = counterpoint_generator.generate_counterpoint_lines(melody)
    print(counterpoint_melody)
except Exception as ex:
    print("An unexpected error occurred:", ex)

class FormStructureGenerator:
    def generate_form_and_structure(self, composition):
        try:
            # Define form structure possibilities
            form_structures = ["AABA", "rondo", "theme_variations"]

            # Choose a random form structure
            form_structure = random.choice(form_structures)

            # Apply the selected form structure to the composition
            if form_structure == "AABA":
                return composition + composition[:2]  # AABA structure
            elif form_structure == "rondo":
                return composition + composition[:1]  # Rondo structure
            elif form_structure == "theme_variations":
                return composition + composition[1:]  # Theme and variations structure

        except Exception as ex:
            raise Exception("An error occurred during form and structure generation: " + str(ex))


# Usage example
try:
    composition = [
        [{"note": 60, "duration": 0.5}, {"note": 62, "duration": 0.5}],
        [{"note": 63, "duration": 0.5}, {"note": 65, "duration": 0.5}]
    ]  # Sample composition
    form_generator = FormStructureGenerator()
    structured_composition = form_generator.generate_form_and_structure(composition)
    print(structured_composition)
except Exception as ex:
    print("An unexpected error occurred:", ex)

class TempoChangeGenerator:
    def introduce_tempo_and_time_signature_changes(self, composition):
        try:
            # Define tempo and time signature possibilities
            tempo_changes = [80, 100, 120]  # BPM values
            time_signature_changes = [("4/4", 4), ("3/4", 3), ("6/8", 6)]  # Time signature and beats per bar

            # Apply tempo and time signature changes to the composition
            for i, section in enumerate(composition):
                # Introduce tempo change with probability
                if random.random() < 0.3:
                    new_tempo = random.choice(tempo_changes)
                    section.append({"type": "tempo", "value": new_tempo})

                # Introduce time signature change with probability
                if random.random() < 0.2:
                    new_time_signature, new_beats = random.choice(time_signature_changes)
                    section.append({"type": "time_signature", "value": new_time_signature, "beats": new_beats})

            return composition
        except Exception as ex:
            raise Exception("An error occurred during tempo and time signature change introduction: " + str(ex))


# Usage example
try:
    composition = [
        [{"note": 60, "duration": 0.5}, {"note": 62, "duration": 0.5}],
        [{"note": 63, "duration": 0.5}, {"note": 65, "duration": 0.5}]
    ]  # Sample composition
    tempo_change_generator = TempoChangeGenerator()
    composition_with_changes = tempo_change_generator.introduce_tempo_and_time_signature_changes(composition)
    print(composition_with_changes)
except Exception as ex:
    print("An unexpected error occurred:", ex)

class AdvancedMusicGenerator:
    def __init__(self):
        # Initialize generator with advanced parameters and settings
        self.chord_generator = ChordGenerator()
        self.melody_generator = MelodyGenerator()
        self.dynamics_generator = DynamicsGenerator()
        self.phrasing_generator = PhrasingGenerator()
        self.cadence_generator = CadenceGenerator()
        self.counterpoint_generator = CounterpointGenerator()
        self.form_generator = FormStructureGenerator()
        self.tempo_change_generator = TempoChangeGenerator()

    def generate_piano_music(self):
        # Generate advanced composition logic using all components
        chord_progression = self.chord_generator.generate_advanced_chord_progression()
        melody = self.melody_generator.generate_melody_with_variations(chord_progression)
        melody_with_dynamics = self.dynamics_generator.apply_dynamics_and_articulation(melody)
        melody_with_phrasing = self.phrasing_generator.introduce_rhythmic_variation(melody_with_dynamics)
        chord_progression_with_cadences = self.cadence_generator.generate_cadences_and_key_changes(chord_progression)
        counterpoint_melody = self.counterpoint_generator.generate_counterpoint_lines(melody_with_phrasing)
        structured_composition = self.form_generator.generate_form_and_structure(counterpoint_melody)
        final_composition = self.tempo_change_generator.introduce_tempo_and_time_signature_changes(
            structured_composition)
        return final_composition


# Usage example
generator = AdvancedMusicGenerator()
composition = generator.generate_piano_music()
print(composition)


def generate_piano_composition(self):
    try:
        # Create instances of all generators
        chord_generator = ChordGenerator()
        melody_generator = MelodyGenerator()
        dynamics_generator = DynamicsGenerator()
        phrasing_generator = PhrasingGenerator()
        cadence_generator = CadenceGenerator()
        counterpoint_generator = CounterpointGenerator()
        form_generator = FormStructureGenerator()
        tempo_change_generator = TempoChangeGenerator()

        # Generate components of the composition
        chord_progression = chord_generator.generate_advanced_chord_progression()
        melody = melody_generator.generate_melody_with_variations(chord_progression)
        composition = {
            "chord_progression": chord_progression,
            "melody": melody
        }
        dynamics_generator.apply_dynamics_and_articulation(composition)
        phrasing_generator.introduce_rhythmic_variation(melody)
        cadence_generator.generate_cadences_and_key_changes(chord_progression)
        counterpoint_generator.generate_counterpoint_lines(melody)
        form_generator.generate_form_and_structure(composition)
        tempo_change_generator.introduce_tempo_and_time_signature_changes(composition)

        return composition
    except Exception as ex:
        raise Exception("An error occurred during composition generation: " + str(ex))


# Usage example
try:
    generator = AdvancedMusicGenerator()
    composition = generator.generate_piano_composition()
    print(composition)
except Exception as ex:
    print("An unexpected error occurred:", ex)
class MIDIExporter:
    def export_to_midi(self, composition, output_directory):
        try:
            # Create a PrettyMIDI object
            midi = pretty_midi.PrettyMIDI()

            # Create an instrument for the piano
            instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Acoustic Grand Piano'))

            # Convert the composition to MIDI events
            time = 0
            for section in composition:
                for event in section:
                    if event["type"] == "note":
                        note = pretty_midi.Note(
                            velocity=64,
                            pitch=event["note"],
                            start=time,
                            end=time + event["duration"]
                        )
                        instrument.notes.append(note)
                    elif event["type"] == "tempo":
                        midi.change_tempo(event["value"], time)
                    elif event["type"] == "time_signature":
                        midi.time_signature_changes.append(
                            pretty_midi.TimeSignature(event["beats"], event["value"]))
                    time += event["duration"]

            # Add the instrument to the MIDI file
            midi.instruments.append(instrument)

            # Save the MIDI file
            midi_filename = os.path.join(output_directory, 'generated_music.mid')
            midi.write(midi_filename)
            return midi_filename

        except Exception as ex:
            raise Exception("An error occurred during MIDI export: " + str(ex))
def main():
    try:
        generator = AdvancedMusicGenerator()
        composition = generator.generate_piano_music()
        print("Generated Composition:")
        print(composition)

        exporter = MIDIExporter()
        script_directory = os.path.dirname(os.path.abspath(__file__))
        midi_filename = exporter.export_to_midi(composition, script_directory)
        print(f"MIDI file '{midi_filename}' saved.")

    except Exception as ex:
        print("An unexpected error occurred:", ex)
        print("Please check your code or consult the library documentation.")

# Entry point of the program
if __name__ == "__main__":
    main()