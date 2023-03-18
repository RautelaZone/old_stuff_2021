package JavaConcepts;

public class InternalWorkingOfHashMap {
    public static void main(String[] args) {
        /*
        HashMap uses its static inner class Node<K,V> for storing map entries. That means each entry in hashMap is a Node.
        Internally HashMap uses a hashCode of the key Object and this hashCode is further used by the hash function to find the index of the bucket where the new entry can be added.
        HashMap uses multiple buckets and each bucket points to a Singly Linked List where the entries (nodes) are stored.
        lOnce the bucket is identified by the hash function using hashcode, then hashCode is used to check if there is already a key with the same hashCode or not in the bucket(singly linked list).
        If there already exists a key with the same hashCode, then the equals() method is used on the keys.
        If the equals() method returns true, that means there is already a node with the same key and hence the value against that key is overwritten in the entry(node),
        otherwise, a new node is created and added to this Singly Linked List of that bucket.
        If there is no key with the same hashCode in the bucket found by the hash function then the new Node is added into the bucket found.

         When we have same hashcode or index then this is the case of Collision.
         In case of hash collision, entry are stored as a node in Linked List and equals() method is used to compare keys.
         The comparison of key is a linear search operation so worst case complexity is O(n).
         So, Java 8 uses the balanced tree instead of Linked List after threshold(8) is reached so complexity reduced to O(log n)

         Hashcode of null value is: 0

         If key given already exists then value is replaced with new value.

         I

         */
    }
}
