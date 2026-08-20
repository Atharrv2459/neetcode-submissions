class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const freq = {}
        for (let i = 0; i < nums.length; i++){
            freq[nums[i]] = (freq[nums[i]] ?? 0) + 1

        }
        for (const [key,value] of Object.entries(freq)){
            if (value > 1){
                return true
            }
        }

    return false
    }
}
