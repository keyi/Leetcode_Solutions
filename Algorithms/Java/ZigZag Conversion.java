public class Solution {
    public String convert(String s, int nRows) {
		if (s == null || nRows < 1) {
			return null;
		}
		if (nRows == 1) {
			return s;
		}
		StringBuilder[] sb = new StringBuilder[nRows];
		for (int i = 0; i < nRows; i++) {
			sb[i] = new StringBuilder();
		}
		boolean flag = false; // false stands for down and true for up
		int pos = 0; // Current position
		for (char c : s.toCharArray()) {
			sb[pos].append(String.valueOf(c));
			if (pos == nRows - 1) {
				flag = true;
			} else if (pos == 0) {
				flag = false;
			}
			if (flag) {
				pos--;
			} else {
				pos++;
			}
		}
		StringBuilder result = sb[0];
		for (int k = 1; k < nRows; k++) {
			result.append(sb[k]);
		}
		return result.toString();

	}
}