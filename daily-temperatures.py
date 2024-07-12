class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #73, 74, 75, 71, 69, 72, 76, 73

        #init the result array of length temp to keep track of days past
        result = [0] * len(temperatures)
        #this stack will store days that have not yet found a hotter day
        stack = [] #pair: [temp, index]

        for i in range(len(temperatures)):
            #compare current temp with stacks current top
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i],i])
        
        return result
