"""
If it’s possible, the final number must be either A[0] or B[0] (pigeonhole-ish: any uniform row must match the first column somewhere)
For a target x, scan once: if neither A[i] nor B[i] is x, impossible; otherwise count flips needed to make all A be x and flips to make all B be x
Try x = A[0] and x = B[0], take the minimum flips among valid options
"""
"""
Time Complexity: O(n) — two linear scans (one per candidate)
Space Complexity: O(1)
"""
class minDomino:
    def minDominoRotations(self, A: list[int], B: list[int]) -> int:
        def rotations_to_make(x: int) -> int:
            flipsA = flipsB = 0
            for a, b in zip(A, B):
                if a != x and b != x:
                    return float('inf')  # impossible for this x
                if a != x: flipsA += 1   # flip A's to x
                if b != x: flipsB += 1   # flip B's to x
            return min(flipsA, flipsB)

        cand1 = rotations_to_make(A[0])
        cand2 = rotations_to_make(B[0])
        ans = min(cand1, cand2)
        return -1 if ans == float('inf') else ans

if __name__ == "__main__":
    obj = minDomino()
    print(obj.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))  # 2
    print(obj.minDominoRotations([3,5,1,2,3],   [3,6,3,3,4]))    # -1
    print(obj.minDominoRotations([1,1,1,1],     [1,1,1,1]))      # 0
    print(obj.minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))  # 1
