class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #first lets simplify input
        cars = []

        for i in range(len(position)):
            time_to_hit = (target - position[i])/speed[i]
            print(time_to_hit)
            cars.append([position[i], speed[i], time_to_hit])

        cars = sorted(cars)

        car_stack = []

        for i in reversed(range(len(cars))):
            car_stack.append(cars[i])
            if len(car_stack) >= 2 and car_stack[-1][2] <= car_stack[-2][2]:
                car_stack.pop()
        
        return len(car_stack)
