function twoSum(nums: number[], target: number): number[] {
    let numIdx = new Map<number, number>()
    for (let i in nums) {
        let id = parseInt(i)
        let diff = target - nums[i]
        if (numIdx.has(diff)) {
            return [numIdx.get(diff) || 0, id]
        }
        numIdx.set(nums[id], id)
    }
    return []
}