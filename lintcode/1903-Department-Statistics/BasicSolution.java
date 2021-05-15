public class BasicSolution {
    /**
     * @param employees:   information of the employees
     * @param friendships: the friendships of employees
     * @return: return the statistics
     */
    public List<String> departmentStatistics(List<String> employees, List<String> friendships) {
        // write your code here.
        //Step 1: loop over employees, get 1: (Engineer, noFriendFromOtherDepartment)
        String[] items;
        Map<String, String[]> employeeMap = new HashMap<String, String[]>();
        for (String line : employees) {
            items = line.split(",\\s+");
            employeeMap.put(items[0], new String[]{items[2], "false"});
        }

        //Step 2: loop over friends, fill noFriendFromOtherDepartment if 1 and 2 are from different department
        String[] departmentWithOtherDepartmentFriend1, departmentWithOtherDepartmentFriend2;
        for (String line : friendships) {
            items = line.split(",\\s+");
            departmentWithOtherDepartmentFriend1 = employeeMap.get(items[0]);
            departmentWithOtherDepartmentFriend2 = employeeMap.get(items[1]);
            if (!departmentWithOtherDepartmentFriend1[0].equals(departmentWithOtherDepartmentFriend2[0])) {
                departmentWithOtherDepartmentFriend1[1] = departmentWithOtherDepartmentFriend2[1] = "true";
            }
        }

        //Step 3: loop over 1: (Engineer, noFriendFromOtherDepartment) --> department: [count, total]
        Map<String, int[]> resList = new HashMap<String, int[]>();
        int[] countWithTotal;

        for (Map.Entry<String, String[]> set : employeeMap.entrySet()) {
            String[] v = set.getValue();

            System.out.println(set.getKey());
            System.out.println(Arrays.toString(set.getValue()));

            if (resList.containsKey(v[0])) {
                countWithTotal = resList.get(v[0]);
            } else {
                countWithTotal = new int[2];
            }
            countWithTotal[1]++;

            if (v[1] == "true") {
                countWithTotal[0]++;
            }
            resList.put(v[0], countWithTotal);
        }
        ;

        //Step 4: output result;
        ArrayList<String> res = new ArrayList<String>();
        for (Map.Entry<String, int[]> set : resList.entrySet()) {
            res.add(set.getKey() + ": " + set.getValue()[0] + " of " + set.getValue()[1]);
        }
        ;

        return res;
    }
}