class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mini=float(inf)
        words=[]
        

        for i in range(len(list1)):
            if list1[i] in list2:
                idx=list2.index(list1[i])
                sum_idx=idx+i
                if mini>=sum_idx:
                    if sum_idx==mini:
                        words.append(list1[i])
                    else:
                        words.clear()
                        words.append(list1[i])
                    mini=sum_idx
                    
                    
        return words
        