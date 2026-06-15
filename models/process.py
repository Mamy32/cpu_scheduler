class Process:

    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = int(arrival)
        self.burst = int(burst)
        self.priority = int(priority)

        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0