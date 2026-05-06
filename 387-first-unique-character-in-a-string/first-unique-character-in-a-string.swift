class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var charToCount = s.reduce(into: [:]) { counts, char in
            counts[char, default: 0] += 1
        }

        for (i, char) in s.enumerated() {
            if charToCount[char] == 1 {
                return i
            }
        }
        return -1
    }
}