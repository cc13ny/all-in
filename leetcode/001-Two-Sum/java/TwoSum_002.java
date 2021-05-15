import java.util.Arrays;
import java.util.Comparator;

class ArrayIndexComparator implements Comparator<Integer> {
    private final int[] array;

    public ArrayIndexComparator(int[] nums) {
        array = nums;
    }

    public int compare(Integer index1, Integer index2) {
        return array[index1] - array[index2];
    }
}


public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Integer[] idx = new Integer[nums.length];
        for (int k = 0; k < idx.length; k++) {
            idx[k] = k;
        }

        Arrays.sort(idx, new ArrayIndexComparator(nums));
        Arrays.sort(nums);

        int i = 0, j = nums.length - 1;
        while (i < j) {
            if (nums[i] + nums[j] < target) {
                i++;
            } else if (nums[i] + nums[j] > target) {
                j--;
            } else {
                if (idx[i] > idx[j]) {
                    res[0] = idx[j] + 1;
                    res[1] = idx[i] + 1;
                } else {
                    res[0] = idx[i] + 1;
                    res[1] = idx[j] + 1;
                }
                break;
            }
        }

        return res;
    }
}
