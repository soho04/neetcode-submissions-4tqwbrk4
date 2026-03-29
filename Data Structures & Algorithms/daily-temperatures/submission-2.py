class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        flag = False
        
        for temp in range(len(temperatures)):

            for i in range(temp, len(temperatures), 1):

                if temperatures[i] > temperatures[temp]:
                    res.append(i - temp)
                    flag = True
                    break

                flag = False


            if not flag:
                res.append('0')
            
            flag = False



        return res
                

