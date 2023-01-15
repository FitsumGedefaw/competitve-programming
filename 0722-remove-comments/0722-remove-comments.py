class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        line = "\n".join(source) + "\n"
        while True:
            single, multiple = line.find('//'), line.find('/*')
            if single == multiple == -1:
                break
            if single == -1 or -1 < multiple < single:
                line = line[: multiple] + line[line.find('*/', multiple + 2) + 2:]
            else:
                line = line[: single] + line[line.find('\n', single + 2) :]
        return list(filter(lambda x: x != '', line.split('\n')))