class Solution {
    public int findKthPositive(int[] arr, int k) {
        List<Integer> complete = IntStream.rangeClosed(1, arr[arr.length-1] + k).boxed().collect(Collectors.toList());
        for (int i : arr) {
            complete.removeAll(Arrays.asList(i));
        }
        System.out.println(complete);
        return (complete.get(k-1));
    }
}
