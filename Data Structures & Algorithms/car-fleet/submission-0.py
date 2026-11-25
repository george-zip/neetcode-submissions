class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), key=lambda p: p[0], reverse=True)
        fleets = []
        for car in cars:
            time = (target - car[0]) / car[1]
            if not fleets:
                fleets.append(time)
            else:
                if time > fleets[-1]:
                    fleets.append(time)
        return len(fleets)