# include "DEMH.hpp"

State::State(int i, std::string c, bool final_state) {
    id = i;
    chord = c;
    is_final_state = final_state;
}

int State::get_id() {
    return id;
}

std::string State::get_chord() {
    return chord;
}

bool State::get_is_final_state() {
    return is_final_state;
}

void State::set_id(int num) {
    id = num;
}

void State::set_chord(std::string c) {
    chord = c;
}

void State::set_is_final_state(bool val) {
    is_final_state = val;
}

void State::set_transitions(std::vector<Transition> new_transitions) {
    transitions = new_transitions;
}

void build_DEMH(std::vector<int> m, std::vector<int> b, std::vector<std::string> t,
          std::vector<std::string> c) {

        // Criar lista de estados
        std::vector<State> st;

        // Criar estado auxiliar para inserção no vetor
        State aux(0, "", 0);

        // Iterar lista de acordes
        for(int i = 0; i <= c.size(); i++) {

            // Atribuir elementos do acorde ao estado auxiliar
            aux.set_id(i);
            aux.set_chord(c.at(i));
            aux.set_is_final_state(i == c.size() ? true : false);

            std::cout << "Estado " << i << ":" <<std::endl;
            std::cout<<"\tid: "<<aux.get_id()<<std::endl;
            std::cout<<"\tchord: "<<aux.get_chord()<<std::endl;
            std::cout<<"\tfinal_state: "<<aux.get_is_final_state()<<std::endl;

            // Configuração de estados
            
            // Adicionar estado na lista de estados
    
        
        }

        // Atribuir lista de estados à classe do DEMH

}
      