class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        data={}
        for i in moves:
            data[i]=data.get(i,0)+1
        if (data.get("R", 0) == data.get("L", 0) and
            data.get("U", 0) == data.get("D", 0)):
            return True
        return False