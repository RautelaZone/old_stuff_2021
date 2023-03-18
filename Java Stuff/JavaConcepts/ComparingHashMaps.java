package JavaConcepts;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class ComparingHashMaps {
    public static void main(String[] args) {
        HashMap<Integer,String> map1= new HashMap<>();
        map1.put(1,"A");
        map1.put(2,"B");
        map1.put(3,"C");
        HashMap<Integer,String> map2= new HashMap<>();
        map2.put(3,"C");
        map2.put(1,"A");
        map2.put(2,"B");
        HashMap<Integer,String> map3= new HashMap<>();
        map3.put(1,"A");
        map3.put(2,"B");
        map3.put(3,"C");
        map3.put(3,"D");
        System.out.println("1) On the basis of Key-Value: use equals method");
        System.out.println("map1 is equal to map2: "+map1.equals(map2));  //true
        System.out.println("map1 is equal to map3: "+map1.equals(map3));  //false

        System.out.println("2) Compare by key: using keySet");
        System.out.println(map1.keySet().equals(map2.keySet()));    //true
        System.out.println(map1.keySet().equals(map3.keySet()));    //true-as keySet gives the set and can't have duplicate

        System.out.println("3) Find out the extra keys");
        HashMap<Integer,String> map4= new HashMap<>();
        map4.put(1,"A");
        map4.put(2,"B");
        map4.put(3,"C");
        map4.put(4,"D");
        // combine the keys from both the maps-using HashSet
        // add the keys from map1
        HashSet<Integer> combinedKeys = new HashSet<>(map1.keySet());
        // add the keys from map4 too
        combinedKeys.addAll(map4.keySet());
        combinedKeys.removeAll(map1.keySet());
        System.out.println("Extra keys are: "+combinedKeys);

        System.out.println("4) Compare by values:");
        HashMap<Integer,String> map5= new HashMap<>();
        map5.put(1,"A");
        map5.put(2,"B");
        map5.put(3,"C");
        HashMap<Integer,String> map6= new HashMap<>();
        map6.put(4,"A");
        map6.put(5,"B");
        map6.put(6,"C");
        HashMap<Integer,String> map7= new HashMap<>();
        map7.put(1,"A");
        map7.put(2,"B");
        map7.put(3,"C");
        map7.put(4,"C");
        System.out.println("4.1) when duplicates are not allowed: Using ArrayList");
        System.out.println(new ArrayList<>(map5.values()).equals(new ArrayList<>(map6.values())));  //true
        System.out.println(new ArrayList<>(map5.values()).equals(new ArrayList<>(map7.values())));  //false
        System.out.println("4.1) when duplicates are allowed: Using HashSet");
        System.out.println(new HashSet<>(map5.values()).equals(new HashSet<>(map6.values())));  //true
        System.out.println(new HashSet<>(map5.values()).equals(new HashSet<>(map7.values())));  //true




    }
}
