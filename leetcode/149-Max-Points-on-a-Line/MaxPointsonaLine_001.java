/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */

public class Solution {
    public int maxPoints(Point[] points) {
        /*Build the unique map for points*/
        
        /**Build the unique map in the form <point.x, <point.y, count>>*/
    	int num = points.length;
    	HashMap<Integer, HashMap<Integer, Integer>> pmap = new HashMap<Integer, HashMap<Integer, Integer>>();
    	for(int i = 0; i < num ; i ++){
    		Point pt = points[i];
    		HashMap<Integer, Integer> pyc = pmap.get(pt.x);// Point yaxis, count
    		if(pyc == null){
    			pyc = new HashMap<Integer, Integer>();
    			pyc.put(pt.y, 1);
    			
    		}
    		else{
    			Integer pc = pyc.get(pt.y);
    			if(pc == null){
    				pyc.put(pt.y, 1);
    			}
    			else{
    				pyc.put(pt.y, pc + 1);
    			}
    		}
    		pmap.put(pt.x, pyc);
    	}
    	
    	/**Build the unique map in the form <Point, count>*/
    	
    	HashMap<Point, Integer> unipmap = new HashMap<Point, Integer>();
    	ArrayList<Point> unipls = new ArrayList<Point>();
    	for(Integer px : pmap.keySet()){
    		HashMap<Integer, Integer> pyc = pmap.get(px);
    		for(Integer py : pyc.keySet()){
    			Point unipt = new Point(px, py);
    			unipls.add(unipt);
    			unipmap.put(unipt, pyc.get(py));//pyc.get(py) --> count
    		}
    	}
    	
    	/*Build the unique direction amap in the form <Angle, <Y-insect, Count>>*/
    	/*Build the unique direction fmap in the form <Angle, <Y-insect, Which-Round>>*/
    	
    	HashMap<Float, HashMap<Float, Integer>> amap = new HashMap<Float, HashMap<Float, Integer>>();
    	HashMap<Float, HashMap<Float, Integer>> fmap = new HashMap<Float, HashMap<Float, Integer>>();
    	
    	int uninum = unipmap.size();//the number of points with unique location
    	int maxcount = 0;//the value returned
    	
    	if(uninum == 1) return unipmap.get(unipls.get(0));
        
        for(int i = 0; i < uninum ; i ++){
        	for(int j = i + 1; j < uninum ; j++){
        		Point pi = unipls.get(i);
        		Point pj = unipls.get(j);
        		float tan = 0;
        		float yinter = 0;
        		
        		if ((pi.x - pj.x) != 0 ){
        			if(pi.x > pj.x){
        				tan = (float)(pi.y - pj.y)/(pi.x - pj.x);
        			}
        			else{
        				tan = (float)(pj.y - pi.y)/(pj.x - pi.x);
        			}
        			yinter = pi.y - pi.x * tan;
        		}
        		else{
        			tan = Float.POSITIVE_INFINITY; 
        			yinter = pi.x;
        		}
        		
        		HashMap<Float, Integer> aymap = amap.get(tan);
        		HashMap<Float, Integer> fymap = fmap.get(tan);
        		if(aymap == null) {
        			aymap = new HashMap<Float, Integer>();
        			fymap = new HashMap<Float, Integer>();
        		}
        		Integer count = aymap.get(yinter);
        		
        		int unipci = unipmap.get(pi);
        		int unipcj = unipmap.get(pj);
        		
        		if (count ==  null ) {
        			count = unipci + unipcj;
        			
        			fymap.put(yinter, i);
                    fmap.put(tan, fymap);
        		}
        		else if(fmap.get(tan).get(yinter) == i){
        			
        			count  = count + unipcj;
        		}
        		
        		if(count > maxcount) maxcount = count;
        		
                aymap.put(yinter, count);
                amap.put(tan, aymap);
        	}
        }

		return maxcount;
    }
}
