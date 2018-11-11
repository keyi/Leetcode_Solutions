public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
			return false;
		}
		long origin = (long) x;
		long res = 0;
		while (origin != 0) {
			res = 10 * res + origin % 10;
			origin /= 10;
		}
		return res == x;
    }
}