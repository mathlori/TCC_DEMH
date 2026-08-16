# include <iostream>
# include <vector>
# include <list>
# include <string>

# include "DEMH.hpp"

int main() {
    std::vector<int> measures = {4};
    std::vector<int> bpms = {120};
    std::vector<std::string> tones = {"Am"};
    std::vector<std::string> chords = {"Am", "F", "C", "G"};
    std::vector<std::string> trs = {"(0|1) [] =4", "(1|2) [] =4", "(2|3) [] =4", "(3|4) [] =4", "(4|1) [] =1", "(4|5) [] =4"};

    build_DEMH(measures, bpms, tones, chords, trs);
}