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

    build_DEMH(measures, bpms, tones, chords);
}