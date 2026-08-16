class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_unsorted = zip(position,speed)
        car_sorted = sorted(car_unsorted)
        cars = car_sorted[::-1]
        fleets = 0
        last_time=0
        for pos, spe in cars:
            time = (target - pos)/spe
            if time > last_time:
                fleets +=1
                last_time = time
        return fleets
        