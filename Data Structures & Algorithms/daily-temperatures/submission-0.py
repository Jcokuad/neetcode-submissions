class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temp, index]
        res = [0] * len(temperatures) # default values of 0 in result

        for i, t in enumerate(temperatures): # i is the index, t is the temp
            while stack and t > stack[-1][0]: # if temp is greater than the last temp in the stack
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
            
