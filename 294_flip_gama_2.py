class Solution:
    def canWin(self, currentState):
        
        def flipit(state):
            if "++" not in state:
                return False
            for i in range(1,len(state)):
                if state[i-1] == state[i] == "+" and not flipit(state[:i-1] + "--" + state[i+1:]):
                    return True
            return False

        return flipit(currentState)
currentState = "+++++++++"
obj = Solution()
print(obj.canWin(currentState))