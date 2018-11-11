public class Solution {
    public String addBinary(String a, String b) {
    	int maxlen = Math.max(a.length(), b.length());
		String res = "";
		int temp = 0;
		int add = 0;
		for (int i = 0; i < maxlen; i++) {
			int x = (i < a.length() ? a.charAt(a.length() - i - 1) - '0' : 0);
			int y = (i < b.length() ? b.charAt(b.length() - i - 1) - '0' : 0);
			temp = (x + y + add) % 2;
			add = (x + y + add) / 2;
			res = temp + res;
		}
		return add == 0 ? res : "1" + res;
        
    }
}