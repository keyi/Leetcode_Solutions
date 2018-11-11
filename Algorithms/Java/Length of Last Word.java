 public class Solution {
    public int lengthOfLastWord(String s) {
        // if (s == "")
		// return 0;
		String[] r = s.trim().split(" ");
		return r[r.length - 1].length();
    }
}