class Solution {

/**
* @param Integer[] $nums
* @param Integer $target
* @return Integer[]
*/
function twoSum($nums, $target) {
$numIdx = array();
foreach (array_values($nums) as $i => $num) {
if (array_key_exists($target - $num, $numIdx)) {
return array($numIdx[$target - $num], $i);
}
$numIdx[$num] = $i;
}
return array(-1, -1);
}
}