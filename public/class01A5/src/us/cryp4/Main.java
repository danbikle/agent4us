/*
Main.java

This Java-app should create and
demonstrate a function which converts a msg into a
random number, r, and SHA-256(r|msg).

Ref:
http://cryp4.us/cclases/class01A#rock
*/

package us.cryp4;

import java.security.MessageDigest;
import java.util.Random;

public class Main {

    public static void main(String[] args) throws Exception
    {
        Random rand       = new Random();
        int hex_size_i    = 64; // Number of places in hex integer.
        char[] hex_char_a = new char[hex_size_i];
        // I should loop through 64 places in a hex integer:
        for (int place_i = 0; place_i < hex_size_i; place_i++) {
            // I should pick a random integer at each place:
            int random_i = rand.nextInt(16);
            // I should convert random_i to a character 0 through f:
            String hex_s = Integer.toHexString(random_i);
            // I should put char-value of random_i at next place:
            hex_char_a[place_i] = hex_s.toCharArray()[0];
        }
        // I should now have 256 bit random-int.
        // I should convert it to readable string:
        String random_s = new String(hex_char_a).toUpperCase();
        System.out.println(random_s);
        String secret_msg    = "paper";
        String random_msg_s  = random_s + secret_msg;
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        digest.update(random_msg_s.getBytes());
        // I should convert to byte-array so I can see it:
        byte hash_b[] = digest.digest();
        // I should convert to String so I can see it:
        String hash_s = javax.xml.bind.DatatypeConverter.printHexBinary(hash_b);
        System.out.println(hash_s);
                
    }
}
