/*
Main.java

This app should start a puzzle using a "Puzzle Friendly"
Cryptographic Hash function named SHA-256.

The idea is very simple; this script should pick a random integer.

Later a contestant will solve the puzzle by guessing the random integer.

Ref:
http://cryp4.us/cclasses/class01A#puzzle
https://www.mkyong.com/java/java-sha-hashing-example/
 */

package us.cryp4;

import java.security.MessageDigest;
import java.util.Random;

public class Main {

    public static void main(String[] args) throws Exception
    {
        Random rand      = new Random();
        Integer range_i  = (int) 1.0e4;
        Integer random_i = rand.nextInt(range_i);
        String in_s      = random_i.toString();
        MessageDigest my_hashlib = MessageDigest.getInstance("SHA-256");
        my_hashlib.update(in_s.getBytes());
        byte digest_b[] = my_hashlib.digest();
        //convert the byte to hex format method 1
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < digest_b.length; i++) {
            sb.append(Integer.toString((digest_b[i] & 0xff) + 0x100, 16).substring(1));
        }
        String digest_s = sb.toString().toUpperCase();
        System.out.println("You should publish this SHA-256 hash-digest. It is a 'Commitment':");
        System.out.println(digest_s);
        System.out.println("Ask contestants to find the integer which created the above digest.");
        System.out.println("The range they should search is 0 through: " + range_i);
        System.out.println("Here is the secret integer you want them to find:");
        System.out.println(random_i);
    }
}
