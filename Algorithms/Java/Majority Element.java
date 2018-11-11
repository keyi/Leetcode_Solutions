public class Solution {
    public int majorityElement(int[] num) {
        int key = num[0];
		int count = 1;
		for (int i = 1; i < num.length; i++) {
			if (num[i] != key) {
				if (count == 0) {
					key = num[i];
					count++;
				} else {
					count--;
				}
			} else {
				count++;
			}
		}
		return key;
    }
}