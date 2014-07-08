/**
 * @author = Chi Chen
 * @email = chenchiapply@gmail.com
 * @version = 1.0
 * @runtime = 392ms
 */
  
/**
 *@description
 *
 * Given a binary tree
 *  
 * struct TreeLinkNode {
 * 	TreeLinkNode *left;
 * 	TreeLinkNode *right;
 * 	TreeLinkNode *next;
 * }
 * 
 * Populate each next pointer to point to its next right node. 
 * If there is no next right node, the next pointer should be set to NULL.
 * Initially, all next pointers are set to NULL.
 *  
 * Note:
 * 	You may only use constant extra space.
 * 	You may assume that it is a perfect binary tree 
 * 	(ie, all leaves are at the same level, and every parent has two children).
 * 	
 * For example,
 * 	Given the following perfect binary tree,
 * 
 * 		  1
 * 		/  \
 *             2    3
 *           / \  / \
 *          4  5  6  7
 *  
 * After calling your function, the tree should look like:
 *    
 *              1 -> NULL
 *            /  \
 *          2 -> 3 -> NULL
 *        / \  / \
 *       4->5->6->7 -> NULL

public class PopulatingNextRightPointersinEachNode {

	public static void main(String[] args) {
		/*Test#0: Null Test*/
		TreeLinkNode nulltest = null;
		connect(nulltest);
		/*Test#1: Simple Test {1,2,3}*/
		TreeLinkNode rt = new TreeLinkNode(1);
		rt.left = new TreeLinkNode(2);
		rt.right = new TreeLinkNode(3);
		connect(rt);
		TreeLinkNode lmc = rt;
		TreeLinkNode p = rt;
		while(lmc != null){
			System.out.print(p.val + ", ");
			p = p.next;
			if(p == null){
				System.out.print("#, ");
				lmc = lmc.left;
				p = lmc;
			}
			
		}

	}

    public static void connect(TreeLinkNode root) {
        TreeLinkNode parent = root;
        if(parent != null){
        
	    	TreeLinkNode child = parent.left;
	    	TreeLinkNode leftmostchild = child;
	    	
	    	while(leftmostchild != null){
	    		if(child == parent.left){
	    			child.next = parent.right;
	    			//System.out.println("Hello");
	    		}
	    		else{
	    			parent = parent.next;
	    			if(parent != null){
	    				child.next = parent.left;
	    			}
	    		}
	    		child = child.next;
	    		
	    		if(child == null){
	    			parent = leftmostchild;
	    			child = parent.left;
	    			leftmostchild = child;
	    		}
	    	}
        }
    }
}
