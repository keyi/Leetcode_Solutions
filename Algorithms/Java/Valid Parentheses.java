public class Solution {
    public boolean isValid(String s) {
		Stack<Character> stack = new Stack<Character>();
		String left = "{[(";
		String right = "}])";
		if (s.length() == 0)
			return true;
		for (int i = 0; i < s.length(); i++) {
			String key = String.valueOf(s.charAt(i));
			if (left.contains(key))
				stack.push(s.charAt(i));
			else if (right.contains(key)) {
				if (stack.isEmpty() || (!isMatch(stack.pop(), s.charAt(i))))
					return false;
			}
		}
		return stack.isEmpty();

	}

	public boolean isMatch(char a, char b) {
		if (a == '[' && b == ']')
			return true;
		if (a == '{' && b == '}')
			return true;
		if (a == '(' && b == ')')
			return true;
		return false;
	}
}