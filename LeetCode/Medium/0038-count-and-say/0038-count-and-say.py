class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        say=self.countAndSay(n-1)
        answer=""
        key=say[0]
        count=1 # 현재까지의 key 개수
        for i in range(1,len(say)):
            if key==say[i]:
                count+=1
            else:
                answer+=str(count)
                answer+=key
                key=say[i]
                count=1
        answer+=str(count)
        answer+=key
        
        return answer