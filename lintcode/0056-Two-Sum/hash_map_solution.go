/**
 * @param numbers: An array of Integer
 * @param target: target = numbers[index1] + numbers[index2]
 * @return: [index1 + 1, index2 + 1] (index1 < index2)
 */
func twoSum (numbers []int, target int) []int {
    // write your code here
    numIdx := make(map[int]int)
    for i, num := range numbers {
        if _, ok := numIdx[target - num]; ok {
            return []int{numIdx[target - num], i}
        }
        numIdx[num] = i
    }
    return nil
}