class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if version1 == version2:
            return 0
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1) == len(v2) and len(v1) == 1:
            if int(version1) < int(version2):
                return -1
            elif int(version1) > int(version2):
                return 1
            else:
                return 0
        for i in range(min(len(v1), len(v2))):
            v1i = int(v1[i])
            v2i = int(v2[i])
            if v1i < v2i:
                return -1
            elif v2i < v1i:
                return 1

        vx = v1 if len(v1) > len(v2) else v2
        if len(v1) != len(v2):
            for i in range(min(len(v1), len(v2)), max(len(v1), len(v2))):
                if int(vx[i]) > 0:
                    return 1 if len(v1) > len(v2) else -1
        return 0


if __name__ == "__main__":
    test_cases = [
        ("1.01", "1.001"),
        ("1.0", "1.0.0"),
        ("0.1", "1.1"),
        ("1.0.1", "1"),
        ("7.5.2.4", "7.5.3"),
    ]
    for test_case in test_cases:
        print(Solution().compareVersion(*test_case))
