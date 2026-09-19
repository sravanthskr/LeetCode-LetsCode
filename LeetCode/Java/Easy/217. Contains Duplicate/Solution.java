import java.util.HashSet;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> st = new HashSet<>();
        for(int num:nums){
            if(st.contains(num)) return true;
            st.add(num);
        }
        return false;
        
        // int n = nums.length;
        // boolean value = false;
        // for(int i=0; i<n; i++){
        //     for(int j=i+1; j<nums.length; j++){
        //         if(nums[i]==nums[j]){
        //             value = true;
        //         }
        //     }
        // }
        // return value;
    }
}