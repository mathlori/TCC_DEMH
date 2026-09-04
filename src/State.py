from Transition import Transition


class State:
	def __init__(self, state_id, chord, final_state):
		self.id = state_id
		self.transitions = []
		self.chord = chord
		self.is_final_state = final_state

    # para adicionar uma transição a lista de transições do estado
	def add_transition(self, transition: Transition):
		self.transitions.append(transition)
