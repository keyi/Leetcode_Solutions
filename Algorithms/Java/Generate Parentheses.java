public class Solution {
    public static ArrayList<String> generateParenthesis(int n) {
		ArrayList<String> ans = new ArrayList<String>();
		getPairs(ans, "", n, n);
		return ans;
	}

	public static void getPairs(ArrayList<String> ans, String s, int left,
			int right) {
		if (left > right || left < 0 || right < 0)
			return;
		if (left == 0 && right == 0) {
			ans.add(s);
			return;
		}
		getPairs(ans, s + "(", left - 1, right);
		getPairs(ans, s + ")", left, right - 1);
	}
}