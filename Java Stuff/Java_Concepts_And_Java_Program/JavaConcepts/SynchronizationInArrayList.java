package com.codewithrautela;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class SynchronizationInArrayList {
    public static void main(String[] args) {

        // 1) By Collections.synchronizedList method--returns the synchronized list
        List<String> nameList = Collections.synchronizedList(new ArrayList<String>());

        // For Add/Remove we don't need explicit synchronization
        nameList.add("Python");
        nameList.add("Java");
        nameList.add("PHP");
        nameList.add("C");
        nameList.add("C#");
        nameList.remove("PHP");

        System.out.println("Synchronization using Collections.synchronizedList method.");

        // To fetch/traverse, we need explicit synchronization
        synchronized (nameList){
            Iterator<String> it= nameList.iterator();
            while (it.hasNext()){
                System.out.println(it.next());
            }
        }
        System.out.println("===========================================");

        // 2) CopyOnWriteArrayList class --> Thread Safe/Synchronized already.
        CopyOnWriteArrayList<String> empList = new CopyOnWriteArrayList<String>();
        empList.add("Anil");
        empList.add("Anil-2");
        empList.add("Anil-3");
        empList.add("Anil-4");
        empList.add("Anil-5");
        empList.remove("Anil");
        System.out.println("Synchronization using CopyOnWriteArrayList Class.");

        // We don't need explicit synchronized for add/remove/traverse
        Iterator<String> it= empList.iterator();
        while (it.hasNext()){
            System.out.println(it.next());
        }



    }
}
