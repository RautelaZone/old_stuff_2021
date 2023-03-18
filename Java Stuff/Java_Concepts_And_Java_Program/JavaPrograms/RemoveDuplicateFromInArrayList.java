package JavaPrograms;
import java.util.*;
import java.util.stream.Collectors;

public class RemoveDuplicateFromInArrayList {
    public static void main(String[] args) {
        System.out.println("Removing duplicate elements from an ArrayList");

        System.out.println("1) Using Simple Compare(With Sort)...");
        int[] arr={16,7,1,2,9,7,6,3,4,1,1,6,4,2,6};
        int[] temp = new int[arr.length];
        Arrays.sort(arr);
        int j=0;
        for(int i=0;i<arr.length-1;i++){
            if(arr[i]!=arr[i+1]){
                temp[j++]=arr[i];
            }
        }

        temp[j++]=arr[arr.length-1];
        for(int i=0;i<j;i++){
            System.out.print(temp[i] +" ");
        }
        System.out.println();
        System.out.println("---------------------");

        System.out.println("2) Using HasMap...");
        int[] arr1 = {16,7,1,2,2,6,2,3,4,5,4,6};
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<arr1.length;i++){
            if(map.containsKey(arr1[i])){
                map.remove(arr1[i]);
            }
            map.put(arr1[i],i);
        }
        map.forEach((k,v)-> System.out.print(k +" "));

        System.out.println();
        System.out.println("---------------------");

        System.out.println("3) Using LinkedHashSet(With Sort)....");
        ArrayList<Integer> numbers = new ArrayList<Integer>(Arrays.asList(16,7,1,2,2,6,2,3,4,5,4,6));
        LinkedHashSet<Integer> linkedHashSet = new LinkedHashSet<Integer>(numbers);
        ArrayList<Integer> numbersWithoutDuplicate = new ArrayList<>(linkedHashSet);
        Collections.sort(numbersWithoutDuplicate);  //will sort
        System.out.println(numbersWithoutDuplicate);

        System.out.println();
        System.out.println("---------------------");

        System.out.println("3) Using Stream-JDK8(With Sort)....");
        ArrayList<Integer> nos = new ArrayList<Integer>(Arrays.asList(16,7,1,2,2,6,2,3,4,5,4,6));
        List<Integer> distinctNos = nos.stream().distinct().collect(Collectors.toList());
        Collections.sort(distinctNos);  //will sort
        System.out.println(distinctNos);





    }
    
}
