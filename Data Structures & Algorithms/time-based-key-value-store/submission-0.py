class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.hash_map.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if timestamp < values[m][1]:
                r = m - 1
            elif timestamp >= values[m][1]:
                l = m + 1
                res = values[m][0]
        return res