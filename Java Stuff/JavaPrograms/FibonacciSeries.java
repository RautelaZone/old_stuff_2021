package JavaPrograms;

public class FibonacciSeries {
    public static void main(String[] args) {
        // 0 1 1 2 3 5 8 13 21
        int i, no1=0, no2=1, sum = 0, range = 10;
        System.out.println(" Fibonacci Series is: ");
        System.out.print(no1+" "+no2);

        for (i=2;i<range;i++){
            sum = no1+no2;
            System.out.print(" "+sum);
            no1 = no2;
            no2 = sum;
        }
    }
}
