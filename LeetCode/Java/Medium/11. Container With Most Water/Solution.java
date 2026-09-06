class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right=height.length-1;
        int maxVal=0;
        while(left<right){
            int w=right-left;
            int h=Math.min(height[left], height[right]);
            int area=w*h;
            maxVal=Math.max(area, maxVal);
            
            if(height[left]<height[right]){
                left++;
            }else{
                right--;
            }

        }
        return maxVal;

        // int maxVal=0;
        // for(int i=0; i<height.length; i++){
        //     for(int j=i+1; j<height.length; j++){
        //         int width = j-i;
        //         int h = Math.min(height[i], height[j]);
        //         int area=width*h;
        //         maxVal=Math.max(area, maxVal);
        //     }
        // }
        // return maxVal;
    }
}