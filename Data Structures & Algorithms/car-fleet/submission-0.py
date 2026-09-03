class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Build a list of (position, arrival time) pairs, one per car
        cars = []

        for i in range(len(position)):
            # Time for this car to reach the target if nothing blocks it
            arrival_time = (target - position[i]) / speed[i]
            cars.append((position[i], arrival_time))

        # Sort by position ascending, so the last entry is the car nearest the target
        cars.sort()

        # Arrival time of the fleet ahead; a car merges into it unless it is slower
        fleet_max = 0

        # Number of distinct fleets that reach the target
        fleet_count = 0

        for i in range(len(cars)):
            # Walk backwards from the car closest to the target
            cur_car = cars.pop()

            # Takes longer than the fleet ahead, so it can never catch up:
            # it starts a new fleet and becomes the blocker for cars behind it
            if cur_car[1] > fleet_max:
                fleet_max = cur_car[1]
                fleet_count += 1

        return fleet_count