public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] ver1 = version1.split("\\.");
		String[] ver2 = version2.split("\\.");
		int len = Math.max(ver1.length, ver2.length);
		for (int i = 0; i < len; i++) {
			int a = i < ver1.length ? Integer.parseInt(ver1[i]) : 0;
			int b = i < ver2.length ? Integer.parseInt(ver2[i]) : 0;
			int flag = a - b;
			if (flag != 0)
				return flag > 0 ? 1 : -1;
		}
		return 0;
    }
}