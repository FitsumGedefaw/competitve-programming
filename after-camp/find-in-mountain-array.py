# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find(start, end, start_val, end_val):
            if end-start==1:
                if start_val==target or end_val==target:
                    return start if start_val==target else end
                return -1
            mid = (start+end)//2
            mid_val = mountain_arr.get(mid)

            if mid_val>=start_val and mid_val>=end_val:
                l = find(start, mid, start_val, mid_val)
                r = find(mid, end, mid_val, end_val)
                return l if l!=-1 else r
            elif mid_val>start_val and mid_val<end_val:
                if mid_val>target:
                    return find(start, mid, start_val, mid_val)
                else:
                    return find(mid, end, mid_val, end_val)
            elif mid_val<start_val and mid_val>end_val:
                if mid_val>target:
                    return find(mid, end, mid_val, end_val)
                else:
                    return find(start, mid, start_val, mid_val)

        n = mountain_arr.length()
        start_val = mountain_arr.get(0)
        end_val = mountain_arr.get(n-1)

        return find(0, n-1, start_val, end_val) 

