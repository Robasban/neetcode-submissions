class TimeMap:

    def __init__(self):
        self.res = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.res:
            self.res[key][timestamp] = value
        else:
            self.res[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        while timestamp > -1:
            if key in self.res and timestamp in self.res[key]:
                return self.res[key][timestamp]
            timestamp -= 1
        return ""
        