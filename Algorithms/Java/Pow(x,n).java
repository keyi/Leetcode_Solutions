public class Solution {
    public double pow(double x, int n) {
    	int k = n;
		double res;
		if (n == 0) {
			return 1;
		}
		if (n == 1) {
			return x;
		}
		if (n < 0) {
			if (n == -2147483648) {
				return pow(1 / x, -n + 2);
			}
			return pow(1 / x, -n);
		} else {
			if (k == -2147483648) {
				res = pow(x * x, n / 2);
				return res * x * x;
			}
			if (n % 2 == 0) {
				return pow(x * x, n / 2);
			} else {
				return pow(x * x, (n - 1) / 2) * x;
			}
		}
        
    }
}