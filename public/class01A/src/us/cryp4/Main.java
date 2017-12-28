/*
This Java app should demo-how-to create a simple hash function.

Solution-Idea:
  - Get the input string, input_s
  - Maybe the string is too short
  - add a 256 bit string to end of input_s 
  - return first 256 bits of input_s

Note that I can create 256 bits from 32 characters which are 8 bytes each.

Linux Demo:

export JAVA_HOME=${HOME}/jdk
export PATH=${JAVA_HOME}/bin:${PATH}

cd to_the_right_folder

javac    src/us/cryp4/Main.java
ls -la   src/us/cryp4/Main.class
java -cp src us.cryp4.Main

*/

package us.cryp4;

public class Main {
    public static String my_hashf(String in_s) {
        // This function should combine in_s with 256 bits.
        String pad64_s = "01234567"; // This is 8 utf-8 characters which is 64 bits.
        // 256 / 64 is 4
        String pad256_s = pad64_s + pad64_s + pad64_s + pad64_s;
        String out_s    = in_s + pad256_s;
        /* I should return the first 256 bits of out_s.
        256 bits is 32 bytes; I should return the first 32 bytes: */
        return out_s.substring(0,32);
    }
    
    public static void main(String[] args) {
        String my_in_s = "Today is Dec 27, 2017 and the weather in California is perfect.";
        String out1_s  = my_hashf(my_in_s);
        System.out.println(out1_s);
	
        my_in_s = "Boston is (16F) cold!";
        String out2_s  = my_hashf(my_in_s);
        System.out.println(out2_s);
	
        my_in_s = "NYC is (20F) cold too!";
        String out3_s  = my_hashf(my_in_s);
        System.out.println(out3_s);
	
        my_in_s = "Sydney looks comfy.";
        String out4_s  = my_hashf(my_in_s);
        System.out.println(out4_s);
    }
}
