class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ans = 0
        cnt = defaultdict(int)
        for num in arr:
            cnt[num] += 1
        i = 0
        while i < len(arr):
            j, k = i, len(arr)-1
            while j < k:
                if arr[i] + arr[j] + arr[k] < target:
                    j += cnt[arr[j]]
                elif arr[i] + arr[j] + arr[k] > target:
                    k -= cnt[arr[k]]
                else:
                    if arr[i] != arr[j] != arr[k]:
                        ans += (cnt[arr[i]] * cnt[arr[j]] * cnt[arr[k]])
                    elif arr[i] == arr[j] != arr[k]:
                        ans += (cnt[arr[i]] * (cnt[arr[i]] - 1) * cnt[arr[k]] // 2)
                    elif arr[i] != arr[j] == arr[k]:
                        ans += (cnt[arr[i]] * cnt[arr[j]] * (cnt[arr[j]] - 1) // 2)
                    else:
                        ans += (cnt[arr[i]] * (cnt[arr[i]] - 1) * (cnt[arr[i]] - 2) // 6)
                    j += cnt[arr[j]]
                    k -= cnt[arr[k]]
            i += cnt[arr[i]]
        return ans % 1000000007
            
