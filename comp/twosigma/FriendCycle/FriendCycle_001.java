public class FriendCircle {
    public static void main(String[] args) {
        char[][] input = {{'Y', 'Y', 'N', 'N'},
                {'Y', 'Y', 'Y', 'N'},
                {'N', 'Y', 'Y', 'N'},
                {'N', 'N', 'N', 'Y'}};
        int count = findFriendCircle(input);
        System.out.println(count);
    }

    public static int findFriendCircle(char[][] input) {
        if (input.length == 0 || input[0].length == 0)
            return 0;

        int n = input.length;
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (input[i][j] == 'Y')
                    uf.union(i, j);
            }
        }

        return uf.getCounts();
    }
}

class UnionFind {
    int[] values;
    int count;

    public UnionFind(int n) {
        values = new int[n];
        for (int i = 0; i < n; i++)
            values[i] = i;
        count = n;
    }

    public void union(int x, int y) {
        int valOfX = this.findRoot(x);
        int valOfY = this.findRoot(y);

        if (valOfX != valOfY) {
            this.values[x] = valOfY;
            this.count -= 1;
        }
    }

    public int findRoot(int x) {
        int px = this.values[x];
        if (px != x)
            this.values[x] = this.findRoot(px);
        return this.values[x];
    }

    public int getCounts() {
        return this.count;
    }
}
