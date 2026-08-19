# include "DEMH.hpp"

DEMH::DEMH(std::vector<int> measures, std::vector<int> bpms, std::vector<std::string> tones,
          std::vector<std::string> chords, std::vector<std::string> transitions) {

        // Criar lista de estados
        std::vector<State> states;

        // Criar estado auxiliar para inserção no vetor
        State aux_state(0, "", 0);

        int chords_size = chords.size();
        int transitions_size = transitions.size();

        // Iterar lista de acordes
        for(int i = 0; i <= chords_size; i++) {

            // Atribuir elementos do acorde ao estado auxiliar
            aux_state.set_id(i);
            aux_state.set_chord(i == chords_size ? "Qf" : chords.at(i));
            aux_state.set_is_final_state(i == chords_size ? true : false);
            
            // Adicionar estado na lista de estados
            states.push_back(aux_state);
        }

        // Configuração de Transições

        Transition aux_transition(0, {0}, 0); // Variável para criar transições

        int origin; // Origem de transição
        int destination; // Final de transição
        float duration; // Duração da transição

        bool measures_verifier = false; // analisar compassos que ocorrem uma transição
        std::vector<int> aux_measures;

        int str_size; // Tamanho da string correpondente à transição

        for(int i = 0; i < transitions.size(); i++) { // Analisar lista de transições
            str_size = transitions.at(i).size();
            for(int j = 0; j < str_size - 1; j++) { // Analisar string com transições
                if(transitions.at(i).at(j+1) == '|')
                    origin = transitions.at(i).at(j) - '0';
                if(transitions.at(i).at(j+1) == ')')
                    destination = transitions.at(i).at(j) - '0';
                if(std::isdigit(transitions.at(i).at(j+1)) && transitions.at(i).at(j) == '=')
                    duration = transitions.at(i).at(j+1) -'0';
                if(transitions.at(i).at(j) == '[')
                    measures_verifier = true;
                if(transitions.at(i).at(j) == ']')
                    measures_verifier = false;
                if(measures_verifier && std::isdigit(transitions.at(i).at(j))) 
                    aux_measures.push_back(transitions.at(i).at(j) - '0');
            }

            // Atribuição da Transição
            aux_transition.set_destination(destination);
            aux_transition.set_duration_time(duration);
            aux_transition.set_measures(aux_measures);

            states[origin].add_transition(aux_transition);
            aux_measures.clear();
        }

        // Impressão de tudo
        for(int i = 0; i < states.size(); i++) {
            std::cout<<"State "<<i<<": "<<std::endl;
            std::cout<<"\tID: "<<states[i].get_id()<<std::endl;
            std::cout<<"\tChord: "<<states[i].get_chord()<<std::endl;
            std::cout<<"\tFinal State: "<<states[i].get_is_final_state()<<std::endl;
            std::cout<<"\tTransitions: "<<std::endl;
            for(int j = 0; j < states[i].get_transitions().size(); j++) {
                std::cout<<"\t\tT"<<j<<":"<<std::endl;
                std::cout<<"\t\t\tDur: "<<states[i].get_transitions()[j].get_duration_time()<<std::endl;
                std::cout<<"\t\t\tDest: "<<states[i].get_transitions()[j].get_destination()<<std::endl;
                std::cout<<"\t\t\tMeasures: ";
                for(int k = 0 ; k < states[i].get_transitions()[j].get_measures().size(); k++) {
                    std::cout<<states[i].get_transitions()[j].get_measures()[k]<<"\t";
                }
                std::cout<<std::endl;
            }
            
            
        }

        // Atribuir lista de estados à classe do DEMH
        this->measures = measures; // compassos
        this->bpms = bpms; // andamentos
        this->tones = tones; // tonalidades
        this->states = states; // estados
        this->initial_state = 0; // estado inicial
        this->final_state = states.size(); // estado final
}
      