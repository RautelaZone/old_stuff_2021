package JavaPrograms;

public class EvenAndOddCount {
    public static void main(String[] args) {
        int num, rem, evenCount, oddCount;
        num = 1224;
        evenCount = 0;
        oddCount = 0;
        while(num>0){
            rem = num%10;
            if (rem%2==0)
                evenCount++;
            else
                oddCount++;
            num = num/10;
        }
        System.out.println("Even number in the digit is: " +evenCount);
        System.out.println("Odd number in the digit is: " +oddCount) ;
    }
}
