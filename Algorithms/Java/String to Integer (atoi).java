public class Solution {

	public static int atoi(String str) {
		String s = new String();
		s = str.trim();
		if (s.length() == 0) {
			return 0;
		}
		int Max = 2147483647;
		int Min = -2147483648;
		long res = 0;
		int flag = 0;
		for (int i = 0; i < s.length(); i++) {
			if (!Character.isDigit(s.charAt(i))) {
				flag = 1;
				break;
			}
		}
		if (flag == 0) {
			for (int i = s.length() - 1; i >= 0; i--) {
				res += (s.charAt(i) - '0') * Math.pow(10, s.length() - i - 1);
			}
			if (res <= Max) {
				return (int) res;
			} else {
				return Max;
			}
		} else {
			if (s.charAt(0) == '+' || s.charAt(0) == '-') {
				if (s.charAt(0) == '-') {
					flag = -1;
				}
				s = s.substring(1, s.length());
			}
		}
		int k = 0;
		while (Character.isDigit(s.charAt(k))) {
			k++;
			if (k >= s.length()) {
				break;
			}
		}
		if (k == 0) {
			return 0;
		} else {
			s = s.substring(0, k);
			res = 0;
			for (int m = s.length() - 1; m >= 0; m--) {
				res += (s.charAt(m) - '0') * Math.pow(10, s.length() - m - 1);
			}
			if (res > Max) {
				if (flag == 1) {
					return Max;
				} else {
					return Min;
				}
			} else {
				return (int) (flag * res);
			}
		}
	}


}
