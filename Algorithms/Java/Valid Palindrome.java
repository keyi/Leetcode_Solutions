public class Solution {
    public boolean isPalindrome(String s) {
        // if (s == "")
		// return true;
		s = s.toLowerCase();
		String ans = "";
		ans = s.replaceAll("[^a-z^0-9]", "");
		for (int i = 0; i < ans.length(); i++) {
			int j = ans.length() - 1 - i;
			if (ans.charAt(i) != ans.charAt(j)) {
				return false;
			}
		}
		return true;
    }
}