use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {

        let mut numIdx: HashMap<i32, i32> = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            if numIdx.contains_key(&(target - num)) {
                return vec![numIdx[&(target - num)], i as i32];
            }
            numIdx.insert(*num, i as i32);
        }
        return vec![-1, -1];
    }
}