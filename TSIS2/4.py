class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        new_max=0
        for x in gain:
            max=max+x
            if(new_max<max):
                new_max = max
        return new_max