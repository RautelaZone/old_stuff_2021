package JavaPrograms;

public class ReversingString {
    public static void main(String[] args) {
        String str = "ABCDE";
        String rev = "";
        int len = str.length();

        // 1) Using concatenation
        for(int i=len-1;i>=0;i--){
            rev = rev+str.charAt(i);
        }
        System.out.println("Reverse string using charAt is:" +rev);

        // 2) Using character Array
        String rev1 = "";
        char a[] = str.toCharArray();
        for(int i=len-1;i>=0;i--){
            rev1 = rev1+str.charAt(i);
        }
        System.out.println("Reverse string using Character Array is:" +rev1);

        // 3) Using String Buffer
        StringBuffer sb = new StringBuffer(str);
        StringBuffer rev2 = sb.reverse();
        System.out.println("Reverse string using String Buffer is:" +rev2);

        // 4) Using StringBuilder
        StringBuilder sb1 = new StringBuilder();
        sb1.append(str);
        StringBuilder rev3 = sb1.reverse();
        System.out.println("Reversed string using String Builder is: "+rev3);

    }
}
