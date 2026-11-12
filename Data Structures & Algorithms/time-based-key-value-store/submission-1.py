from collections import namedtuple

Entry = namedtuple("Entry", "timestamp,value")

class TimeMap:

    def __init__(self):
        self.entries_by_key: dict[str, list[Entry]] = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.entries_by_key:
            self.entries_by_key[key] = []
        self.entries_by_key[key].append(
            Entry(timestamp, value)
        )

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.entries_by_key:
            return ""
        entries = self.entries_by_key[key]
        if timestamp < entries[0].timestamp:
            return ""
        lo, hi = 0, len(entries) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if entries[mid].timestamp == timestamp:
                return entries[mid].value
            elif entries[mid].timestamp > timestamp:
                hi = mid - 1
            else:
                lo = mid + 1
        return entries[lo - 1].value if lo > 0 else entries[lo].value
        
