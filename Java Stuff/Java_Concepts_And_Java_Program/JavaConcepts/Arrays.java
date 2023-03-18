package com.codewithrautela;

public class Arrays {
    public static void main(String[] args) {

        // Single Dimensional Array
        int [] nos = {23,32,43,54,34,32,11};
        System.out.println("Printing values using traditional for loop...");
        for(int i=0;i<nos.length;i++){
            System.out.println("Value "+i+" is: "+nos[i]);
        }

        System.out.println("Printing values using foreach loop...");
        System.out.println("Values are:");
        for(int value:nos) {
            System.out.println(value);
        }
        // Two Dimensional Arrays
        int [][] matrix ={{1,2,3,4},{5,6,7,8}};
        System.out.println(matrix[0][2]);
        System.out.println("Printing 2D Matrix using for loop:");
        for(int i=0;i<matrix.length;i++){
            for (int j=0;j<matrix[i].length;j++){
                System.out.print(matrix[i][j]+" ");
            }
        }
    }
}
