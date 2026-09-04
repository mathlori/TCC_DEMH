import re
import time
from State import State
from Transition import Transition


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
		current_state = self.initial_state
		current_measure = 1
		current_beat = 1
		current_time_signature_id = 0
		current_bpm_id = 0
		current_tone_id = 0

		while current_state != self.final_state:
			time.sleep(60 / self.bpms[current_bpm_id])
			current_beat += 1

			if current_beat > self.time_signature[current_time_signature_id]:
				current_beat = 0
				current_measure += 1

			print(f"> COMPASSO {current_measure}, TEMPO {current_beat}")

            # IMPLEMENTAR TRANSIÇÃO DE ESTADOS
			# Lógica:

            # Inicializar choosen_score e choosen (verificar se alguma transição for escolhida)
            # Iterar cada transição do estado
                # inicializar score de gatilhos

                # Verificar se algum dos compassos de gatilho da transicao[i] é igual ao compasso atual
                    # Se for, incrementar score de gatilhos

                # Verificar se algum dos beats de gatilho da transição[i] é igual ao beat atual
                    # Se for, incrementar score de gatilhos
					
                # Se o score atual for maior que o escolhido, substituir
                    # Atribuir transição à variavel choosen (transição foi escolhida)
				
                # Verificar se até o momento não foi escolhido uma transição (ou seja, o score permanece em zero)
                    # Se sim, verificar se ambas as transições não tem gatilho

            # Se até houver uma transição escolhida
                # Fazer atribuições conforme novo estado
				# Sinalizar alterações de assinatura, bpm e compasso
