package JavaConcepts;

import java.util.Comparator;
import java.util.Set;
import java.util.TreeMap;

public class TreeMapConcept {
    public static void main(String[] args) {
        /*
        Java TreeMap class is a red-black tree based implementation
        TreeMap implements SortedMap
        It provides an efficient means of storing key-value pairs in sorted order.
        Java TreeMap contains values based on the key
        Java TreeMap contains only unique elements.
        Java TreeMap cannot have a null key but can have multiple null values.
        Java TreeMap is non synchronized
        Java TreeMap maintains ascending order.
         */
        System.out.println("Tree Map sorts the data as per key in ascending order");
        TreeMap<Integer, String> map = new TreeMap<>();
        map.put(1000,"Tom");
        map.put(3000,"Peter");
        map.put(2000,"Anil");
        map.put(11000,"Steeve");
        map.put(400,"Robby");
        map.forEach((k,v) -> System.out.println("Key: "+k+" and value: "+v));

        System.out.println(map.lastKey()); // will give last key
        System.out.println(map.firstKey()); // will give first key

        System.out.println(map.firstEntry()); // will give first key-value
        System.out.println(map.lastEntry()); // will give last key-value

        // To print all keys which are less than 3000
        Set<Integer> keyLessThan3K = map.headMap(3000).keySet();
        System.out.println("All keys which are less than 3000: ");
        System.out.println(keyLessThan3K);


        // To print all keys which are greater than 3000
        Set<Integer> keyGrtThan3K = map.tailMap(3000).keySet();
        System.out.println("All keys which are equal and greater than 3000: ");
        System.out.println(keyGrtThan3K);

        System.out.println("Printing data in descending/reverse order:");
        TreeMap<Integer, String> map1 = new TreeMap<>(Comparator.reverseOrder());
        map1.put(1000,"Tom");
        map1.put(3000,"Peter");
        map1.put(2000,"Anil");
        map1.put(11000,"Steeve");
        map1.put(400,"Robby");
        map1.forEach((k,v) -> System.out.println("Key: "+k+" and value: "+v));
    }
}
