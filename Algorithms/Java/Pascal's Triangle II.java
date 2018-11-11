public class Solution {
    public List<Integer> getRow(int rowIndex) {
		List<List<Integer>> ans = new ArrayList<List<Integer>>();
		List<Integer> s = new ArrayList<Integer>();
		s.add(1);
		ans.add(s);
		rowIndex++;
		for (int i = 1; i < rowIndex; i++) {
			List<Integer> prev = ans.get(i - 1);
			List<Integer> curr = new ArrayList<Integer>();
			for (int j = 0; j <= i; j++) {
				if (j == 0 || j == i)
					curr.add(1);
				else
					curr.add(prev.get(j - 1) + prev.get(j));
			}
			ans.add(curr);
		}
		return ans.get(rowIndex - 1);
	}
}