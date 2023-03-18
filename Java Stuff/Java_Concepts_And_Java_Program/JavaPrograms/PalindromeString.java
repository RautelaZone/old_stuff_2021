package JavaPrograms;

import java.util.Scanner;

public class PalindromeString {
    public static void main(String[] args) {
        System.out.println("Enter a string: ");
        Scanner sc = new Scanner(System.in);
        String str,originalStr;
        str = sc.next();
        originalStr = str;
        System.out.println("Original string is:" + originalStr);
        String rev = "";
        int len = str.length();

        // 1) Using concatenation
        for(int i=len-1;i>=0;i--){
            rev = rev+str.charAt(i);
        }
        System.out.println("Reversed string is:" + rev);
        if (originalStr.equals(rev))
                System.out.println("String is palindrome");
        else
            System.out.println("String is not palindrome");
    }
}
