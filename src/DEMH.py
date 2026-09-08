import re
import musicpy
from musicpy import chord, note, play

from State import State
from Transition import Transition
from ChordDictionary import ChordDictionary


class DEMH:
	def __init__(self, input_file):
		with open(input_file, "r") as file:
			print(f"> File {input_file} opened!")

			section = -1
			sections = [[], [], [], [], []]
			for line in file:
				line = line.strip()
				if line in ["[TIME_SIGNATURE]", "[BPMS]", "[TONES]", "[CHORDS]", "[TRANSITIONS]"]:
					section += 1
				elif line:
					sections[section].append(line)

		self.time_signature = [int(value) for value in sections[0]]
		self.bpms = [int(value) for value in sections[1]]
		self.tones = sections[2]
		chords = sections[3]

		self.states = [
			State(state_id, chord, False)
			for state_id, chord in enumerate(chords)
		]
		self.states.append(State(len(chords), "Qf", True))
		self.initial_state = 0
		self.final_state = len(self.states) - 1

		for transition_text in sections[4]:
			match = re.fullmatch(
				r"\((\d+)\s*\|\s*(\d+)\)"
				r"(?:\s+TRIGGERS\s*=\s*\[\s*MEASURES\s*:\s*\(([^)]*)\)\s*,?\s*BEATS\s*:\s*\(([^)]*)\)\s*\])?"
				r"(?:\s+CHANGES\s*=\s*\{\s*TIME_SIGNATURE\s*:\s*([^\s}]*)\s+BPM\s*:\s*([^\s}]*)\s+TONE\s*:\s*([^\s}]*)\s*\})?",
				transition_text,
			)
			if match is None:
				raise ValueError(f"Invalid transition: {transition_text}")

			(
				origin,
				destination,
				trigger_measure_text,
				trigger_beat_text,
				new_time_signature,
				new_bpm,
				new_tone,
			) = match.groups()

			trigger_measure = [
				int(value.strip())
				for value in (trigger_measure_text or "").split(",")
				if value.strip()
			]
			trigger_beat = [
				int(value.strip())
				for value in (trigger_beat_text or "").split(",")
				if value.strip()
			]

			self.states[int(origin)].add_transition(
				Transition(
					trigger_measure,
					int(destination),
					int(new_time_signature) if new_time_signature else 0,
					int(new_bpm) if new_bpm else 0,
					int(new_tone) if new_tone else 0,
					trigger_beat,
				)
			)

		print("> DEMH LIDO COM SUCESSO!")

	def print_demh(self):
		for state in self.states:
			print(f"State {state.id}:")
			print(f"\tID: {state.id}")
			print(f"\tChord: {state.chord}")
			print(f"\tFinal State: {int(state.is_final_state)}")
			print("\tTransitions:")

			for index, transition in enumerate(state.transitions):
				print(f"\t\tT{index}:")
				print(f"\t\t\tDest: {transition.destination}")
				print(f"\t\t\tTrigger measure IDs: {transition.trigger_measure}")
				print(f"\t\t\tTrigger beat IDs: {transition.trigger_beat}")
				print(f"\t\t\tChanges: TIME_SIGNATURE={transition.new_time_signature} BPM={transition.new_bpm} TONE={transition.new_tone}")

	def execute(self):
		if not musicpy.has_audio_interface:
			raise RuntimeError(
				"A saída de áudio não foi inicializada pelo pygame. "
				"Verifique o dispositivo de som do Windows."
			)
		musicpy.pygame.mixer.music.set_volume(1.0)
		print("> Execução do DEMH foi iniciada!")
		current_state = self.initial_state
		current_measure = 1
		current_beat = 1
		current_time_signature_id = 0
		current_bpm_id = 0
		current_tone_id = 0

		# Inicialização de dicionário de acordes para as músicas
		chord_dict = ChordDictionary()

		while current_state != self.final_state:
			# Toca o acorde durante o beat atual
			midi_notes = chord_dict.chord[self.states[current_state].chord]
			musicpy_notes = []
			for midi_note in midi_notes:
				current_note = note("C", num=4)
				current_note.degree = midi_note
				musicpy_notes.append(current_note)
			current_chord = chord(musicpy_notes)
			
			play(
				current_chord,
				bpm=self.bpms[current_bpm_id],
				save_as_file=False,
				wait=True,
			)
			print(f"> COMPASSO {current_measure}, TEMPO {current_beat}")
			print(f"--- ACORDE: {self.states[current_state].chord}")

			# O play(wait=True) aguarda o beat terminar.
			last_beat = self.time_signature[current_time_signature_id]
			was_last_beat = current_beat == last_beat

			if was_last_beat:
				current_measure += 1
				current_beat = 1
			else:
				current_beat += 1

			# Seleciona a transição que deve valer na próxima posição
			choosen_score = 0
			choosen_transition = None

			for transition in self.states[current_state].transitions:
				# Transições padrão só ocorrem depois do último beat
				if not transition.trigger_measure and not transition.trigger_beat:
					if was_last_beat and choosen_transition is None:
						choosen_transition = transition
					continue

				t_score = 0

				# Gatilhos de compasso apontam para o início do novo estado
				for measure in transition.trigger_measure:
					if measure == current_measure and current_beat == 1:
						t_score += 1

				for beat in transition.trigger_beat:
					if beat == current_beat:
						t_score += 1

				if t_score > choosen_score:
					choosen_score = t_score
					choosen_transition = transition

			if choosen_transition is not None:
				print(f"\t-Executando transição para estado {choosen_transition.destination}")
				current_state = choosen_transition.destination

				# Sinalizar alterações de assinatura, BPM e tom
				if choosen_transition.new_time_signature != current_time_signature_id:
					old_value = self.time_signature[current_time_signature_id]
					new_value = self.time_signature[choosen_transition.new_time_signature]
					print(
						f"\t- Houve uma mudança de assinatura de tempo: "
						f"de {old_value}/4 para {new_value}/4."
					)
					current_time_signature_id = choosen_transition.new_time_signature

				if choosen_transition.new_bpm != current_bpm_id:
					old_value = self.bpms[current_bpm_id]
					new_value = self.bpms[choosen_transition.new_bpm]
					print(
						f"\t- Houve uma mudança de andamento: "
						f"de {old_value}bpm para {new_value}bpm."
					)
					current_bpm_id = choosen_transition.new_bpm

				if choosen_transition.new_tone != current_tone_id:
					old_value = self.tones[current_tone_id]
					new_value = self.tones[choosen_transition.new_tone]
					print(
						f"\t- Houve uma mudança de tom: "
						f"de {old_value} para {new_value}."
					)
					current_tone_id = choosen_transition.new_tone
        
