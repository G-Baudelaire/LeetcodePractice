class RecentCounter:

    def __init__(self):
        self.data = []

    def ping(self, t: int) -> int:
        self.data.append(t)

        new_start = 0
        for time in self.data:
            if time >= t - 3000:
                break
            new_start += 1
            
        self.data = self.data[new_start:]
        return len(self.data)
