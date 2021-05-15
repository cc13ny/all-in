func twoSum(nums []int, target int) []int {
numIdx := make(map[int]int)
for i, num := range nums {
if _, ok := numIdx[target - num]; ok {
return []int{numIdx[target - num], i}
}
numIdx[num] = i
}
return nil
}
