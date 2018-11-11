public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
		if (prices.length < 2)
			return profit;
		int maximum = prices[0], minimum = prices[0];
		for (int x : prices) {
			if (x < minimum) {
				minimum = x;
				maximum = x;
			} else if (x >= maximum) {
				maximum = x;
				profit = (maximum - minimum) > profit ? maximum - minimum
						: profit;
			}
		}
		return profit;
    }
}