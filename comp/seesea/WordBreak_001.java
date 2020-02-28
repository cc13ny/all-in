import java.util.ArrayList;

public class IsFormedFromDict {
	public static ArrayList<String> radixsort(ArrayList<String> strs){
		return strs;
	}
	
	public static boolean isformed(String str, ArrayList<String> dict){
		int strlen = str.length();
		if(strlen == 0)
			return true;
					
		for(String word : dict){
			int wdlen = word.length();
			if(strlen >= wdlen){			
				if(str.substring(0, wdlen).equals(word)){
					if(isformed(str.substring(wdlen, strlen), dict))
						return true;
				}
			}
		}
		return false;
	}

	public static void main(String[] args) {
		
		ArrayList<String> strs = new ArrayList<String>();
		strs.add("HELICOPTER");
		strs.add("ABCD");
		strs.add("HELICOER");
		strs.add("HELICOPTERLIPTER");
		strs = radixsort(strs);
		
		ArrayList<String> dict = new ArrayList<String>();
		dict.add("HE");
		dict.add("LI");
		dict.add("C");
		dict.add("O");
		dict.add("PT");
		dict.add("ER");
		
		int len = 0;
		String res = "";
		for(String str : strs){
			if(str.length() > len && isformed(str, dict)){
				len = str.length();
				res = str;
			}
		}
		
		System.out.println(res);
	}
}
