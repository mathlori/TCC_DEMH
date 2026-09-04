class Transition:
    def __init__(self, trigger_measure=None, destination=0,
                 time_signature=0, new_bpm=0, new_tone=0,
                 trigger_beat=None):

        self.trigger_measure = list(trigger_measure or [])
        self.trigger_beat = list(trigger_beat or [])
        self.destination = destination

        # Alterações de métricas durante a música
        self.new_time_signature = time_signature
        self.new_bpm = new_bpm
        self.new_tone = new_tone

