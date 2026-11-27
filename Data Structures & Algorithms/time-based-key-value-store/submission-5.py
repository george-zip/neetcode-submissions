class TimeMap:

    def __init__(self):
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        answer = ""
        if key in self.cache:
            values = self.cache[key]
            # print(f"{key=},{timestamp=},{values=}")
            lo, hi = 0, len(values) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                # print(f"{mid=},{values[mid][0]=}")
                if values[mid][0] == timestamp:
                    return values[mid][1]
                elif values[mid][0] > timestamp:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # print(f"{lo=}")
            if lo > 0:
                answer = values[lo - 1][1]
        return answer
