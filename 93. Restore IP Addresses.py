from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):
                        if i + j + k + l == len(s):
                            I = int(s[:i])
                            J = int(s[i : i + j])
                            K = int(s[i + j : i + j + k])
                            L = int(s[i + j + k : i + j + k + l])
                            if I <= 255 and J <= 255 and K <= 255 and L <= 255:
                                ip = f"{I}.{J}.{K}.{L}"
                                if len(ip) == len(s) + 3:
                                    ips.append(ip)
        return ips


if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
