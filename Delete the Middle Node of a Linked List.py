class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        bans,arr = [0,0],[]
        for  i in range(len(senate)):
            arr.append( 0 if senate[i]=='R' else 1 )
        while( len(set(arr)) > 1 ):
            temp = []
            for c in arr:
                if bans[c] >0:bans[c]-=1
                else:
                    temp.append(c)
                    bans[~c]+=1 
            arr = []
            for c in temp:
                if bans[c] >0:bans[c]-=1
                else:arr.append(c)
        
        return 'Radiant' if arr[0] == 0 else 'Dire'
            
