# pragma once

# include <iostream>
# include <string>
# include <vector>

class Transition {
    private:
        float duration_time;
        std::vector<int> measures;
        int destination;
};

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

        void set_id(int num);

        void set_chord(std::string c);
        
        void set_is_final_state(bool val);

        void set_transitions(std::vector<Transition> new_transitions);
};

class DEMH {
    private:
        std::vector<int> measures; // compassos
        std::vector<int> bpms; // andamentos
        std::vector<char> tones; // tonalidades

        std::vector<State> states; // estados
        int initial_state; // estado inicial
        int final_state; // estado final
    
    /*
    public:
        DEMH(std::vector<int> m, std::vector<int> b, std::vector<char> t,
             std::vector<State> s, int initial, int final);
    */   
};

void build_DEMH(std::vector<int> m, std::vector<int> b, std::vector<std::string> t,
          std::vector<std::string> c);