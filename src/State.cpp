# include "State.hpp"

State::State(int i, std::string c, bool final_state) {
    id = i;
    chord = c;
    is_final_state = final_state;
}

int State::get_id() {
    return this->id;
}

std::string State::get_chord() {
    return this->chord;
}

bool State::get_is_final_state() {
    return this->is_final_state;
}

std::vector<Transition> State::get_transitions() {
    return this->transitions;
}

void State::set_id(int id) {
    this->id = id;
}

void State::set_chord(std::string chord) {
    this->chord = chord;
}

void State::set_is_final_state(bool is_final_state) {
    this->is_final_state = is_final_state;
}

void State::add_transition(Transition transition) {
    this->transitions.push_back(transition);
}