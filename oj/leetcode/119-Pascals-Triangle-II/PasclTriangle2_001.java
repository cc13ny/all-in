import java.util.ArrayList;

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        
        List<Integer> row = new ArrayList<Integer>();
        if(rowIndex == 0){
            row.add(1);
            return row;
        }  
        List<Integer> prerow = getRow(rowIndex - 1);
        
        row.add(1);
        row.add(1);
                
        for(int j = 1; j < rowIndex; j++){
            int num = prerow.get(j-1) + prerow.get(j);
            row.add(j, num);
        }
        
        return row;
    }
    
}
