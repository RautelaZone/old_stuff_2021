package com.codewithrautela;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class HashMapConcept {
    public static void main(String[] args) {
        // stores data in the form of key-value pair
        // no order
        // can not access using index
        // not thread safe-not synchronized
        // key can not be duplicate-wont give error but latest value will be updated
        // can store n number of null values
        // can have only one null key-wont give error but latest value will be updated
        // can not use iterator directly to hashmap instead use it on keySet or keyValue
        // Initial capacity of HashMap is 16(buckets/segments) with Load Factor 0.75

        HashMap<String,String> capitalMap = new HashMap<>();
        capitalMap.put("India","New Delhi");
        capitalMap.put("USA","Washington DC");
        capitalMap.put("UK","London");
        capitalMap.put("Russia",null);
        capitalMap.put("Pakistan",null);
        capitalMap.put(null,"Bangladesh");
        capitalMap.put("Pakistan","Afghanistan");
        System.out.println(capitalMap.get("India"));
        System.out.println(capitalMap.get("USA"));
        System.out.println(capitalMap.get("UK"));
        System.out.println(capitalMap.get("Russia"));
        System.out.println(capitalMap.get("Pakistan"));
        System.out.println(capitalMap.get(null));

        capitalMap.put("UK","LondonUpdated");   // will update this value so key can't be duplicate
        System.out.println(capitalMap.get("UK"));

        capitalMap.put(null,"BangladeshUpdated");   // will update this value so can't have more than one null key
        System.out.println(capitalMap.get(null));

        capitalMap.remove("Pakistan");  // will delete the particular value and will give null
        System.out.println("Value of key-Pakistan after remove method: "+capitalMap.get("Pakistan"));

        System.out.println("==============Traversing in HashMap=============");
        System.out.println("1) Iterator: Using keySet...");
        Iterator<String> it = capitalMap.keySet().iterator();
        while (it.hasNext()){
            String key = it.next();
            String values = capitalMap.get(key);
            System.out.println("Key: "+key+ " and Value: "+values);
        }
        System.out.println("2) Iterator: Using entrySet...");
        Iterator<Map.Entry<String,String>> it1 = capitalMap.entrySet().iterator();
        while (it1.hasNext()){
            Map.Entry<String, String> entry = it1.next();
            System.out.println("Key: "+entry.getKey()+ " and Value: "+entry.getValue());
        }

        System.out.println("3) Iterator: From Java8, using forEach and Lambda...");
        capitalMap.forEach((k,v)-> System.out.println("Key: "+k+ " and Value: "+v));





    }
}
