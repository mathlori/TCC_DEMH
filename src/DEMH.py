import re

from State import State
from Transition import Transition


class DEMH: # Construtor
	def __init__(self, input_file):

		# Abertura do arquivo de entrada
		with open(input_file, "r") as f:
			print(f"> File {input_file} opened!")

			section = -1 # seção atual sendo lida no arquivo
			sections = [[], [], [], [], []]
			for line in f:
				# altera a seção lida do arquivo
				if line in ["[MEASURES]\n", "[BPMS]\n", "[TONES]\n", "[CHORDS]\n", "[TRANSITIONS]\n"]:
					section+=1
				elif line != "\n":
					sections[section].append(line.replace('\n', ''))


			# Atribuição das variáveis do estado
			
			self.measures = sections[0] # compassos
			self.bpms = sections[1] # bpms
			self.tones = sections[2] # tons da música

			chords = sections[3] # acordes da música
			transitions = sections[4] # transições do DEMH
		
			self.states = [ # iteração pela lista de acordes para atribuir os estados
				State(state_id, chord, False)
				for state_id, chord in enumerate(chords)
			]
			
			# Adição do estado final
			final_state_id = len(chords)
			self.states.append(State(final_state_id, "Qf", True))

			# Adição do estado inicial
			self.initial_state = 0
			self.final_state = len(self.states)

			# Varredura das strings de transição
			for transition_text in transitions:

				# faz o match com o formato (x | y) [z*] = w
				match = re.fullmatch(
					r"\((\d+)\|(\d+)\)\s*\[([^]]*)\]\s*=\s*(\d+(?:\.\d+)?)",
					transition_text.strip(),
				)

				# Se não for válido
				if match is None:
					raise ValueError(f"Invalid transition: {transition_text}")

				# Atribui os valores às variáveis conforme a string
				origin, destination, measures_text, duration = match.groups()
				transition_measures = [
					int(value.strip())
					for value in measures_text.split(",")
					if value.strip()
				]

				# Adiciona as transições aos respectivos estados
				self.states[int(origin)].add_transition(
					Transition(float(duration), transition_measures, int(destination))
				)
				
			print("> DEMH LIDO COM SUCESSO!")

	def print_demh(self):
		# Iteração para cada estado
		for state in self.states:
			print(f"State {state.get_id()}:")
			print(f"\tID: {state.get_id()}")
			print(f"\tChord: {state.get_chord()}")
			print(f"\tFinal State: {int(state.get_is_final_state())}")
			print("\tTransitions:")

            # Iteração para cada transição
			for index, transition in enumerate(state.get_transitions()):
				print(f"\t\tT{index}:")
				print(f"\t\t\tDur: {transition.get_duration_time():g}")
				print(f"\t\t\tDest: {transition.get_destination()}")
				measures = "\t".join(str(value) for value in transition.get_measures()) # compassos
				print(f"\t\t\tMeasures: {measures}\t")
