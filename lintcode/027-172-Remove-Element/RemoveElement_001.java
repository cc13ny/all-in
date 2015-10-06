// Maybe we don't need "elemqueue"

public class Solution {
    /** 
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    public int removeElement(int[] A, int elem) {
        
        int newlen = A.length; // decrement it by 1 each time when elem is visited
        ArrayList<Integer> elemqueue = new ArrayList<Integer> (); // a queue to record available locations to be filled
        
        /*
         * If it is equal to elem, just skip.
         * Otherwise, it's assigned into the first available index
         */
        for (int i = 0; i < A.length; i++) {
            if (A[i] == elem) {
                newlen--;
                elemqueue.add(i);
            } else if (!elemqueue.isEmpty()) {
            	int next = elemqueue.remove(0);
            	A[next] = A[i];
            	elemqueue.add(i);
            }
        }
        return newlen;
    }
}