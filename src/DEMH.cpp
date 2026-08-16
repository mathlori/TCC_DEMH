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

void build_DEMH(std::vector<int> me, std::vector<int> bp, std::vector<std::string> tn,
          std::vector<std::string> ch, std::vector<std::string> trs) {

        // Criar lista de estados
        std::vector<State> st;

        // Criar estado auxiliar para inserção no vetor
        State aux(0, "", 0);

        int chords_size = ch.size();
        int transitions_size = trs.size();

        // Iterar lista de acordes
        for(int i = 0; i <= chords_size; i++) {

            // Atribuir elementos do acorde ao estado auxiliar
            aux.set_id(i);
            aux.set_chord(i == chords_size ? "Qf" : ch.at(i));
            aux.set_is_final_state(i == chords_size ? true : false);
            
            // Adicionar estado na lista de estados
            st.push_back(aux);

            // Log do estado
            std::cout << "Estado " << i << " adicionado:" <<std::endl;
            std::cout<<"\tid: "<<st[i].get_id()<<std::endl;
            std::cout<<"\tchord: "<<st[i].get_chord()<<std::endl;
            std::cout<<"\tfinal_state: "<<st[i].get_is_final_state()<<std::endl;
        }

        // Configuração de Transições
        int org; // Origem de transição
        int dest; // Final de transição
        int dur; // Duração da transição

        int str_size; // Tamanho da string correpondente à transição

        for(int i = 0; i < 1; i++) {
            str_size = trs.at(i).size();
            for(int j = 0; j < str_size - 1; j++) {
                if(trs.at(i).at(j+1) == '|')
                    org = trs.at(i).at(j) - '0';
                if(trs.at(i).at(j+1) == ')')
                    dest = trs.at(i).at(j) - '0';
                if(std::isdigit(trs.at(i).at(j+1)) && trs.at(i).at(j) == '=')
                    dur = trs.at(i).at(j+1) -'0';
            }
        }

        std::cout<<"Origem: "<<org<<std::endl;
        std::cout<<"Destino: "<<dest<<std::endl;
        std::cout<<"Duracao: "<<dur<<std::endl;

        // Atribuir lista de estados à classe do DEMH

}
      