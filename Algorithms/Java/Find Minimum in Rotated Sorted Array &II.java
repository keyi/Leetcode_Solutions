public class Solution {
    public int findMin(int[] num) {
        int left = 0;
		int right = num.length - 1;
		while (left < right && num[left] >= num[right]) {
			int mid = (left + right) / 2;
			if (num[mid] > num[left])
				left = mid + 1;
			else if (num[mid] < num[right])
				right = mid;
			else
				left += 1;
		}
		return num[left];
    }
}