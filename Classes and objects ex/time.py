class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours, new_minutes, new_seconds):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def update_valid_time(self):
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1

                if self.hours > Time.max_hours:
                    self.hours = 0

    def next_second(self):
        self.seconds += 1
        self.update_valid_time()

        return self.get_time()
