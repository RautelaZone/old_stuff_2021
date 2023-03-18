package com.codewithrautela;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class ComparingTwoArrayLists {
    public static void main(String[] args) {
        System.out.println("1) Sort and then use equals...");
        ArrayList<String> l1 = new ArrayList<>(Arrays.asList("A","B", "C", "D"));
        ArrayList<String> l2 = new ArrayList<>(Arrays.asList("A","D", "B", "C"));
        Collections.sort(l1);
        Collections.sort(l2);
        System.out.println("Both array lists are equal? -- "+ l1.equals(l2));

        System.out.println("2) Find out additional elements...");
        ArrayList<String> l3 = new ArrayList<>(Arrays.asList("A","B", "C", "F"));
        ArrayList<String> l4 = new ArrayList<>(Arrays.asList("A","C", "B", "E"));
        Collections.sort(l3);
        Collections.sort(l4);
        l3.removeAll(l4);
        System.out.println("Additional Elements Are:" + l3);

        System.out.println("3) Find out missing elements...");
        ArrayList<String> l5 = new ArrayList<>(Arrays.asList("A","B", "C", "F"));
        ArrayList<String> l6 = new ArrayList<>(Arrays.asList("A","C", "B", "E"));
        Collections.sort(l5);
        Collections.sort(l6);
        l6.removeAll(l5);
        System.out.println("Missing Elements Are:" + l6);

        System.out.println("4) Find out common elements...");
        ArrayList<String> l7 = new ArrayList<>(Arrays.asList("A","B", "C", "F"));
        ArrayList<String> l8 = new ArrayList<>(Arrays.asList("A","C", "B", "E"));
        Collections.sort(l7);
        Collections.sort(l8);
        l7.retainAll(l8);
        System.out.println("Common Elements Are:" + l7);



    }
}
