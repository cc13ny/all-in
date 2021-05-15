public class HashMapSolution {
    /**
     * @param numbers: An array of Integer
     * @param target:  target = numbers[index1] + numbers[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        Map<Integer, Integer> numberIdx = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers.length; i++) {
            if (numberIdx.containsKey(target - numbers[i])) {
                return new int[]{numberIdx.get(target - numbers[i]), i};
            }
            numberIdx.put(numbers[i], i);
        }
        return new int[2];
    }
}