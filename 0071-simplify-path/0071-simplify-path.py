class Solution(object):
    def simplifyPath(self, path):
        st = deque()
        for part in path.split("/"):
            if part == "" or part ==".":
                continue
            elif part == "..":
                if st:
                    st.pop()
            else:
                st.append(part)
        return "/" + "/".join(st)
                