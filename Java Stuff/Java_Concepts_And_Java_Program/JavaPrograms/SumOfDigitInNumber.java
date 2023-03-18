package JavaPrograms;

public class SumOfDigitInNumber {
    public static void main(String[] args) {
        int num = 133023;
        int sum=0;
        while(num>0){
            sum = sum+num%10;
            num = num/10;
        }
        System.out.println("Sum of digit in the number is: "+sum);
    }
}
