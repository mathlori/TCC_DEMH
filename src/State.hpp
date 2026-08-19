# pragma once

# include "Transition.hpp"
# include "libs.hpp"

class State {
    private:
        int id;
        std::vector<Transition> transitions;
        std::string chord;
        bool is_final_state; 
    public:
        State(int i, std::string c, bool final_state);

        int get_id();

        std::string get_chord();

        bool get_is_final_state();

        std::vector<Transition> get_transitions();

        void set_id(int id);

        void set_chord(std::string chord);
        
        void set_is_final_state(bool is_final_state);

        void add_transition(Transition transition);
};