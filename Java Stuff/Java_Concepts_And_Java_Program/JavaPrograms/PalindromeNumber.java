package JavaPrograms;

import java.util.Scanner;

public class PalindromeNumber {
    public static void main(String[] args) {
        System.out.println("Enter a number: ");
        Scanner sc = new Scanner(System.in);
        int num,originalNo;
        num = sc.nextInt();
        originalNo = num;
        System.out.println("Original No is:" + originalNo);
        int rev = 0;
        while(num!=0){
            rev = rev*10+num%10;
            num = num/10;
        }
        System.out.println("Reversed No is:"+ rev);
        if (originalNo==rev)
            System.out.println("Number is palindrome");
        else
            System.out.println("Number is not palindrome");
    }
}
