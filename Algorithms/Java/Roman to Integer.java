public class Solution {
    public int romanToInt(String s) {
        int res = 0;
		int flag;
		int[] num = { 1000, 500, 100, 50, 10, 5, 1 };
		String roman = "MDCLXVI";
		for (int i = s.length() - 1; i >= 0; i--) {
			flag = 1;
			char k = s.charAt(i);
			String m = String.valueOf(k);
			if ("CXI".contains(m) && (res >= 5 * num[roman.indexOf(k)])) {
				flag = -1;
			}
			res += (flag * num[roman.indexOf(k)]);
		}
		return res;
    }
}