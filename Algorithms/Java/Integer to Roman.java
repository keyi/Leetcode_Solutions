public class Solution {
    public String intToRoman(int num) {
        int[] integer = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
		String[] roman = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X",
				"IX", "V", "IV", "I" };
		String res = "";
		int i = 0;
		int amount;
		while (true) {
			amount = num / integer[i];
			num %= integer[i];
			while (amount > 0) {
				res += roman[i];
				amount--;
			}
			i++;
			if (num == 0) {
				break;
			}
		}
		return res;
        
    }
}