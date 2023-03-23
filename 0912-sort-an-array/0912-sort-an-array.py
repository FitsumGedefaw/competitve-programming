class Solution:
    def mergeSort(self, left, right, arr):
        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)

        return merge(left_half, right_half)
    
    def merge(self, leftArr, rightArr):
        ptr1 = ptr2 = 0
        res = []

        while ptr1 < len(leftArr) or ptr2 < len(rightArr):
            if ptr1 < len(leftArr) and not ptr2 < len(rightArr):
                res.append(leftArr[ptr1])
                ptr1 += 1

            elif not ptr1 < len(leftArr) and ptr2 < len(rightArr):
                res.append(rightArr[ptr2])
                ptr2 += 1

            else:
                if leftArr[ptr1] <= rightArr[ptr2]:
                    res.append(leftArr[ptr1])
                    ptr1 += 1
                else:
                    res.append(rightArr[ptr2])
                    ptr2 += 1
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0, len(nums)-1, nums)
        