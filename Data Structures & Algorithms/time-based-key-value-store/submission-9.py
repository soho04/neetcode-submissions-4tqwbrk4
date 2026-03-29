class TimeMap:

    def __init__(self):
        self.structure = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.structure[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        value_list = self.structure[key]
        left, right = 0, len(value_list)-1

        while left <= right:

            mid = (left + right) // 2

            if value_list[mid][1] <= timestamp:
                res = value_list[mid][0]
                left = mid + 1

            else:
                right = mid - 1

        return res

        # [ (value1, 10), ]

       #    lm          r
       # [ (happy, 1), (sad, 3) ]