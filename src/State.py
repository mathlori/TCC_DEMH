from Transition import Transition


class State:
	def __init__(self, state_id, chord, final_state):
		self.id = state_id
		self.transitions = []
		self.chord = chord
		self.is_final_state = final_state

    # getters e setters
	def get_id(self):
		return self.id

	def get_chord(self):
		return self.chord

	def get_is_final_state(self):
		return self.is_final_state

	def get_transitions(self):
		return self.transitions

	def set_id(self, state_id):
		self.id = state_id

	def set_chord(self, chord):
		self.chord = chord

	def set_is_final_state(self, is_final_state):
		self.is_final_state = is_final_state

    # para adicionar uma transição a lista de transições do estado
	def add_transition(self, transition: Transition):
		self.transitions.append(transition)
