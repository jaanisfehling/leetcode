public class Solution {
    public int LengthOfLongestSubstring(string s) {
        List<char> used = new List<char> {};
        int res = 0;
        for (int i=0; i<s.Length; ++i) {
            for (int j=i; j<s.Length; ++j) {
                if (used.Contains(s[j])) {
                    break;
                }
                else {
                    used.Add(s[j]);
                }
                foreach (char c in used) {
                }
            }
            res = Math.Max(res, used.Count);
            used = new List<char> {};
        }
        return res;
    }
}
