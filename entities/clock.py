import time


class Clock:
    def __init__(self, cycles_per_second):
        self.cycles_per_second = cycles_per_second
        self.reset()

    def has_ticked(self) -> bool:
        """Returns True if clock has ticked (new cycle has begun)"""
        if time.time_ns() > self.next_tick:
            self.reset()
            return True
        return False

    def reset(self):
        self.next_tick = time.time_ns() + (1000 * 1000 * 1000) / self.cycles_per_second
