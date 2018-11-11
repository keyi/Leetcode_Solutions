public class Solution {
    public int sqrt(int x) {
        if (x < 4) {
			return x == 0 ? 0 : 1;
		}
		int left, right, mid, last = 0;
		left = 2;
		right = x / 2;
		while (left <= right) {
			mid = (left + right) / 2;
			if (Math.pow(mid, 2) == x) {
				return mid;
			} else if (Math.pow(mid, 2) > x) {
				right = mid - 1;
				last = right;
			} else {
				left = mid + 1;
				last = mid;
			}
		}
		return last;
    }
}