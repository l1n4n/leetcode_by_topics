public class Solution{
   
        public int mySqrt(int x) {
            int left = 1, right = x;
            int mid;
            if (x < 1) {
                return 0;
            }
            while (left <= right) {
                mid = left + (right - left) / 2;
                if (mid == x / mid) {
                    return mid;
                } else if (mid < x / mid) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
               
            }
            return left-1; //largest integer <= sqrt(x)
        }

    
     public static void main(String []args){
        Solution s = new Solution();
        System.out.println(s.mySqrt(10));
     }
}

class Solution {
    public int mySqrt(int x) {
        if (x < 1) {
            return 0;
        }
        long guess = x; // in case of integer overflow
        while (guess > x / guess) {
            guess = (guess + x / guess) / 2;
        }
        return (int)guess;
    }
}