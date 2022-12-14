public class Solution {
    public string IntToRoman(int num) {
        var romans = new Dictionary<int, char>(){
            {1000, 'M'},
            {500, 'D'},
            {100, 'C'},
            {50, 'L'},
            {10, 'X'},
            {5, 'V'},
            {1, 'I'}
        };
        string final = "";
        foreach (KeyValuePair<int, char> item in romans) {
            int n = num / item.Key;
            num = num % item.Key;
            final += String.Concat(Enumerable.Repeat(item.Value, n));
            if (num >= 900) {
                final += "CM";
                num -= 900;
            }
            else if (num >= 400 && num < 500) {
                final += "CD";
                num -= 400;
            }
            else if (num >= 90 && num < 100) {
                final += "XC";
                num -= 90;
            }
            else if (num >= 40 && num < 50) {
                final += "XL";
                num -= 40;
            }
            else if (num == 9) {
                final += "IX";
                num -= 9;
            }
            else if (num == 4) {
                final += "IV";
                num -= 4;
            }
        }
        return final;
    }
}
