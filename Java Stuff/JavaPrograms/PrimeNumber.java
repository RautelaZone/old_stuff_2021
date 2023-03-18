package JavaPrograms;

import java.util.Scanner;

public class PrimeNumber {
    public static void main(String[] args) {
        System.out.println("Enter a number to check for Prime: ");
        int num, i , count = 0;
        Scanner sc = new Scanner(System.in);
        num = sc.nextInt();
        if(num>1)
        {
            for(i=1; i<=num; i++){
                if(num%i==0)
                    count++;
            }
            if(count==2)
                System.out.println(num+" is a Prime number.");
            else
                System.out.println(num+" is a Not Prime number.");
        }
        else
            System.out.println(num+" is a Not Prime number.");
    }
}
