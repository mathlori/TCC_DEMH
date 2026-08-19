# include "Transition.hpp"

Transition::Transition(float duration_time, std::vector<int> measures, int destination) {
    this->duration_time = duration_time;
    this->measures = measures;
    this->destination = destination;
}

float Transition::get_duration_time() {
    return this->duration_time;
}

std::vector<int> Transition::get_measures() {
    return this->measures;
}

int Transition::get_destination() {
    return this->destination;
}

void Transition::set_duration_time(float duration_time) {
    this->duration_time = duration_time;
}

void Transition::set_measures(std::vector<int> measures) {
    this->measures = measures;
}

void Transition::set_destination(int destination) {
    this->destination = destination;
}