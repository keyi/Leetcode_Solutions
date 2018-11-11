public class Solution {
    public String reverseWords(String s) {
        String[] scut = s.trim().split(" +");
		String res = "";
		int length = scut.length;
		for (int i = 0; i < length; i++) {
			res += scut[length - i - 1];
			if (i != scut.length - 1)
				res += " ";
		}
		return res;
    }
}

			// ANOTHET METHOD //
// public class Solution {
//     public String reverseWords(String s) {
//         String[] scut = s.trim().split(" +");
// 		StringBuilder res = new StringBuilder();
// 		int length = scut.length;
// 		for (int i = 0; i < length; i++) {
// 			res.append(scut[length - i - 1]);
// 			if (i != length - 1)
// 				res.append(" ");
// 		}
// 		return res.toString();
//     }
// }