package JavaPrograms;

import java.util.Scanner;

public class ReversingNumber {
    public static void main(String[] args) {
        // 1) Using Logic
        int num = 467321;
        int rev = 0;
        while(num!=0){
            rev = rev*10+num%10;
            num = num/10;
        }
        System.out.println("Reversed num using Logic is: "+rev);

        // 2) Using StringBuffer
        int num1 = 467321;
        StringBuffer sb = new StringBuffer(String.valueOf(num1));
        StringBuffer rev1 = sb.reverse();
        System.out.println("Reversed num using String Buffer is: "+rev1);

        // 2) Using StringBuilder
        int num2 = 467321;
        StringBuilder sb1 = new StringBuilder();
        sb1.append(num2);
        StringBuilder rev2 = sb1.reverse();
        System.out.println("Reversed num using String Builder is: "+rev2);

    }
}
