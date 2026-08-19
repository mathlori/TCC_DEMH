# pragma once

# include "State.hpp"
# include "Transition.hpp"

# include "libs.hpp"

class DEMH {
    private:
        std::vector<int> measures; // compassos
        std::vector<int> bpms; // andamentos
        std::vector<std::string> tones; // tonalidades

        std::vector<State> states; // estados
        int initial_state; // estado inicial
        int final_state; // estado final
    
    
    public:
        DEMH(std::vector<int> measures, std::vector<int> bpms, std::vector<std::string> tones,
          std::vector<std::string> chords, std::vector<std::string> transitions);
};

