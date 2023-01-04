class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = {
            "1": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "10#": "j",
            "11#": "k",
            "12#": "l",
            "13#": "m",
            "14#": "n",
            "15#": "o",
            "16#": "p",
            "17#": "q",
            "18#": "r",
            "19#": "s",
            "20#": "t",
            "21#": "u",
            "22#": "v",
            "23#": "w",
            "24#": "x",
            "25#": "y",
            "26#": "z",
        }
        
        s_deque = deque(s)
        corresponding_letters = deque()
        
        while s_deque:
            if s_deque[-1] == "#":
                code = ""
                for i in range(3):
                    code = s_deque.pop() + code
                
                corresponding_letters.appendleft(alphabet[code])
            
            else: 
                code = s_deque.pop()
                
                corresponding_letters.appendleft(alphabet[code])
        
        return "".join(corresponding_letters)
                
                
                
        