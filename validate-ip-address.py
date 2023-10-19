class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count(".") > 0:
            return self.validateIPv4(queryIP)
        return self.validateIPv6(queryIP)
    
    def validateIPv4(self, ip):
        ip = ip.split(".")
        if len(ip) != 4:
            return "Neither"
        for bit in ip:
            if not bit.isnumeric() or (bit[0] == "0" and len(bit) > 1) or int(bit) < 0 or int(bit) > 255:
                return "Neither"
        return "IPv4"

    def validateIPv6(self, ip):
        allowedChars = list("abcdefABCDEF")
        ip = ip.split(":")
        if len(ip) != 8:
            return "Neither"
        for bit in ip:
            if len(bit) < 1 or len(bit) > 4:
                return "Neither"
            for char in bit:
                if char.isnumeric() or char in allowedChars:
                    continue
                return "Neither"
        return "IPv6"