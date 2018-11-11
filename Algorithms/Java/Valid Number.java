public class Solution {
    public boolean isNumber(String s) {
    	boolean num = false;
		boolean dot = false;
		boolean exp = false;
		String scut = s.trim();
		int length = scut.length();
		for (int i = 0; i < length; i++) {
			char c = scut.charAt(i);
			if (c == '.') {
				if (exp || dot) {
					return false;
				}
				dot = true;
			} else if (c <= '9' && c >= '0')
				num = true;
			else if (c == '+' || c == '-') {
				if (i != 0 && scut.charAt(i - 1) != 'e')
					return false;
			} else if (c == 'e') {
				if ((!num) || exp) {
					return false;
				}
				num = false; // "2e2" is valid but "2e" is not.
				exp = true;
			} else
				return false;
		}
		return num;
    }
}