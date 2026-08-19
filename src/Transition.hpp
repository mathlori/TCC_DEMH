# pragma once

# include "libs.hpp"

class Transition {
    private:
        float duration_time;
        std::vector<int> measures;
        int destination;
    public:
        Transition(float duration_time, std::vector<int> measures, int destination);

        float get_duration_time();

        std::vector<int> get_measures();

        int get_destination(); 

        void set_duration_time(float duration_time);

        void set_measures(std::vector<int> measures);

        void set_destination(int destination);
};