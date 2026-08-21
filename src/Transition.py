class Transition:
    def __init__(self, duration_time, measures, destination):
        self.duration_time = duration_time
        self.measures = list(measures)
        self.destination = destination

    # getters e setters
    def get_duration_time(self):
        return self.duration_time

    def get_measures(self):
        return self.measures

    def get_destination(self):
        return self.destination

    def set_duration_time(self, duration_time):
        self.duration_time = duration_time

    def set_measures(self, measures):
        self.measures = list(measures)

    def set_destination(self, destination):
        self.destination = destination