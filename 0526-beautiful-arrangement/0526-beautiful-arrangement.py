class Solution:
    def countArrangement(self, n: int) -> int:
        n += 1
        def backTrack(index, seen):
            if index == n:
                return 1

            num = 0
            for i in range(1, n):
                if i not in seen and (i % index == 0 or index % i == 0):
                    seen.add(i)
                    num += backTrack(index + 1, seen)
                    seen.remove(i)

            return num

        return backTrack(1, set())