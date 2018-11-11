public class Solution {
    public int reverse(int x) {
    	long key = (long) x;
		long ans = 0;
		int flag = 1;
		String s;
		if (key < 0) {
			key = -key;
			flag = -1;
		}
		s = String.valueOf(key);
		int[] res = new int[s.length()];
		for (int i = 0; i <= s.length() - 1; i++) {
			res[i] = s.charAt(s.length() - 1 - i) - '0';
		}
		for (int i = res.length - 1; i >= 0; i--) {
			ans += res[res.length - 1 - i] * Math.pow(10, i);
		}
		ans *= flag;
		if (ans < -2147483648 || ans > 2147483647) {
			return 0;
		} else {
			return (int) ans;
		}
        
    }
}