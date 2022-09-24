# BFS时可能会有重复的状态，比如baaba要变为abaab
# b和第一个a交换，得到ababa
# b和第二个a交换，得到aabba；第二个a再和第一个b交换，得到ababa
# 状态重复，所以需要用hash表存储状态，不重复搜索

class Solution:
    def gen_s(self, s, i, j):
        l = list(s)
        l[i], l[j] = l[j], l[i]
        return ''.join(l)

    def kSimilarity(self, s1: str, s2: str) -> int:
        vis = {s1}
        q = deque([(s1, 0)])
        while q:
            s, depth = q.popleft()
            for i in range(len(s)):
                if s[i] == s2[i]:
                    continue
                for j in range(i + 1, len(s)):
                    if s[j] == s2[i]: # 由于字符串中可能有重复字符，所以满足这一条件的可能不止一个，需要BFS
                        new_s = self.gen_s(s, i, j)
                        if new_s not in vis:
                            q.append((new_s, depth + 1))
                            vis.add(new_s)
                else:
                    break
            else:
                return depth