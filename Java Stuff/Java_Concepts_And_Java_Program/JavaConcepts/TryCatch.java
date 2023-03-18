package com.codewithrautela;

public class TryCatch {
    public static void main(String[] args) {
        String[] vehicle = {"Maruti","Renault","Ford","Mahindra","Tata","Honda"};
        try{
            System.out.println(vehicle[9]);
        }
        catch (Exception e){
            System.out.println("Error: "+e);
        }
        System.out.println("This line will execute as try catch will not stop the program if any error occurs.");
    }
}
