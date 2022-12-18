public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int i1 = 0;
        int i2 = 0;
        int[] mergedArray = new int[nums1.Length + nums2.Length];
        while (i1 <= nums1.Length && i2 <= nums2.Length) {
            if (i1 == nums1.Length && i2 == nums2.Length) {
                break;
            }
            else if (i1 == nums1.Length) {
                mergedArray[i1 + i2] = nums2[i2];
                i2++;
            }
            else if (i2 == nums2.Length) {
                mergedArray[i1 + i2] = nums1[i1];
                i1++;
            }
            else if (nums1[i1] <= nums2[i2]) {
                mergedArray[i1 + i2] = nums1[i1];
                i1++;
            }
            else if (nums2[i2] < nums1[i1]) {
                mergedArray[i1 + i2] = nums2[i2];
                i2++;
            }
        }
        if (mergedArray.Length % 2 == 0) {
            return (double)(mergedArray[mergedArray.Length/2-1] + mergedArray[mergedArray.Length/2]) / 2;
        }
        else {
            return mergedArray[mergedArray.Length/2];
        }
    }
}
