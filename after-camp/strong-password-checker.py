class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        conditions = [False, False, False]
        for ch in password:
            if ch.islower():
                conditions[0] = True
            elif ch.isupper():
                conditions[1] = True
            elif ch.isdigit():
                conditions[2] = True

        unmetConditions = len([c for c in conditions if c == False])

        length = len(password)
        numOfSteps = 0
        i = 0
        repeatedSeqs = []
        while i < len(password):
            if i + 2 < len(password) and password[i] == password[i+1] == password[i+2]:
                rep = 3
                j = i + 3
                while j < len(password) and password[j] == password[j-1]:
                    rep, j = rep + 1, j + 1
                repeatedSeqs.append( (rep % 3, rep) )
                i = j

            else:
                i += 1

        heapq.heapify(repeatedSeqs)
        while repeatedSeqs:
            rem, ct = heapq.heappop(repeatedSeqs)
            numOfSteps += 1

            if length < 6:
                length += 1
                unmetConditions -= 1
                if ct >= 5:
                    heapq.heappush(repeatedSeqs, ((ct - 2) % 3, ct - 2))

            elif length > 20:
                length -= 1
                if ct >= 4:
                    heapq.heappush(repeatedSeqs, ((ct - 1) % 3, ct - 1))    

            elif unmetConditions > 0:
                unmetConditions -= 1
                if ct >= 6:
                    heapq.heappush(repeatedSeqs, ((ct - 3) % 3, ct - 3))
                        
            else:
                if ct >= 6:
                    heapq.heappush(repeatedSeqs, ((ct - 3) % 3, ct - 3))
        
        if length > 20:
            numOfSteps += (length - 20)

        elif length < 6:
            numOfSteps += (6 - length)
            unmetConditions -= (6 - length)

        return numOfSteps + (unmetConditions if unmetConditions > 0 else 0)

        

        





        