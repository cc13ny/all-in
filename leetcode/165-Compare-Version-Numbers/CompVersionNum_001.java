public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] parts1 = version1.split("\\.");
        String[] parts2 = version2.split("\\.");

        int size1 = parts1.length;
        int size2 = parts2.length;
        int min = 0;
        if (size1 < size2) {
            min = size1;
        } else {
            min = size2;
        }

        int i = 0;

        while (i < min) {
            int a = Integer.parseInt(parts1[i]);
            int b = Integer.parseInt(parts2[i]);

            if (a < b) {
                return -1;
            } else if (a > b) {
                return 1;
            }

            i++;
        }

        if ((size1 == min) && (size2 == min)) {
            return 0;

        }

        if (size1 > min) {

            for (int j = min; j < size1; j++) {
                int c = Integer.parseInt(parts1[j]);
                if (c != 0) {
                    return 1;
                }
            }
        } else {
            for (int j = min; j < size2; j++) {
                int c = Integer.parseInt(parts2[j]);
                if (c != 0) {
                    return -1;
                }
            }
        }

        return 0;
    }
}
