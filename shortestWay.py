"""
Trace through source left-right, matching as many characters of target as we can in one pass (a subsequence)
Each full pass over source contributes one to the answer; repeat passes until the whole target is consumed
If in a pass we can’t match anything (because the next target char isn’t in source), return -1
"""
"""
Time Complexity: O(ans · |source|) (each pass scans source;)
Space Complexity: O(1)
"""
class shortestWay:
    def shortestWayString(self, source: str, target: str) -> int:
        src_set = set(source)
        for ch in target:
            if ch not in src_set:
                return -1

        ans = 0
        i = 0 
        n = len(target)

        while i < n:
            ans += 1
            j = 0 
            progressed = False
            while j < len(source) and i < n:
                if source[j] == target[i]:
                    i += 1
                    progressed = True
                j += 1

            if not progressed:
                return -1

        return ans

if __name__ == "__main__":
    print(shortestWay().shortestWayString("abc", "abcbc"))     # 2  ("abc" + "bc")
    print(shortestWay().shortestWayString("abc", "acdbc"))     # -1 (d not in source)
    print(shortestWay().shortestWayString("xyz", "xzyxz"))     # 3
    print(shortestWay().shortestWayString("abc", "abcbc"))    # 2
