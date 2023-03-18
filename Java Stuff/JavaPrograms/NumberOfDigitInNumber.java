package JavaPrograms;

public class NumberOfDigitInNumber {
    public static void main(String[] args) {
        int num, count;
        num = 324512;
        count = 0;
        while(num>0){
            num = num/10;
            count++;
        }
        System.out.println("No of digits in number is: "+count);
    }
}
