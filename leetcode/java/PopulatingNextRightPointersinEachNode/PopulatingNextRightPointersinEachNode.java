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
