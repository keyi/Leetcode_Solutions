public class Solution {

    public String convertToTitle(int n) {
    	String result;
        if (n == 0) {
            return "";
        } else {
            n--;
            return convertToTitle(n / 26) + (char) ('A' + n % 26);
        }

    }

}