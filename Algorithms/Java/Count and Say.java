public class Solution {
    public String countAndSay(int n) {
        String ans = "1";
		for (int i = 1; i < n; i++) {
			String s = ans;
			ans = "";
			int index = 0;
			for (int j = 0; j < s.length(); j++) {
				int count = 0;
				char curr = s.charAt(index);
				while (index < s.length() && s.charAt(index) == curr) {
					count++;
					index++;
				}
				ans = ans + String.valueOf(count) + String.valueOf(curr);
				if (index == s.length())
					break;
			}
		}
		return ans;
    }
}