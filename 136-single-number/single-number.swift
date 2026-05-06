class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
         2 * Set(nums).reduce(0, +) - nums.reduce(0, +)
    }
}