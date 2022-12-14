public class Solution {
    public string LongestPalindrome(string s) {
        char firstC = s[0];
        bool cancelFlag = true;
        foreach (char c in s) {
            if (!c.Equals(firstC)) {
                cancelFlag = false;
                break;
            }
        }
        if (cancelFlag) return s;
        string test_string = "";
        string res = "";
        var dict = new Dictionary<string, bool>();
        bool palin;
        for (int i=0; i<s.Length; ++i) {
            for (int j=i; j<s.Length; ++j) {
                test_string += s[j];
                if (dict.ContainsKey(test_string)) {
                    res = dict[test_string] && res.Length < test_string.Length ? test_string : res;
                }
                else {
                    palin = isPalindrome(test_string);
                    if(palin && res.Length < test_string.Length) {
                        res = test_string;
                        dict.Add(res, palin);
                    }
                }
            }
            if (res.Length > s.Length-i) return res;
            test_string = "";
        }
        return res;
    }
    public bool isPalindrome(string s) {
        if (s.Length < 2) return true;
        if (!s[0].Equals(s[s.Length-1])) return false;
        char[] half = s.Substring(0, (s.Length/2)).ToCharArray();
        Array.Reverse(half);
        char[] second_half;
        if (s.Length % 2 == 0) {
            second_half = s.Substring((s.Length/2), (s.Length/2)).ToCharArray();
        }
        else {
            second_half = s.Substring((s.Length/2)+1, (s.Length/2)).ToCharArray();
        }
        if (new string(half).Equals(new string(second_half))) {
            return true;
        }
        else {
            return false;
        }
    }
}
