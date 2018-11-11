public class Solution {
    public int findPeakElement(int[] num) {
        int length = num.length;
		if (length == 1)
			return 0;
		else {
			for (int i = 0; i < length; i++) {
				if (i == 0) {
					if (num[i] > num[i + 1])
						return i;
				} else if (i == length - 1) {
					if (num[i] > num[i - 1])
						return i;
				} else if (num[i] > num[i - 1] && num[i] > num[i + 1])
					return i;
			}
		}
		return 0;
    }
}