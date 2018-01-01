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

public class Main {

    public static void main(String[] args) throws Exception
    {
        Integer range_i      = (int) 1.0e4;
        Integer random_i     = 8613;
        String in_s      = random_i.toString();
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(in_s.getBytes());
        byte byteData[] = md.digest();
        //convert the byte to hex format method 1
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < byteData.length; i++) {
            sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16).substring(1));
        }
        String digest_s = sb.toString();
        System.out.println("Hex format : " + sb.toString());
        System.out.println("You should publish this SHA-256 hash-digest. It is a 'Commitment':");
        System.out.println(digest_s);
        System.out.println("Ask contestants to find the integer which created the above digest.");
        System.out.println("The range they should search is 0 through: " + range_i);
        System.out.println("Here is the secret integer you want them to find:");
        System.out.println(random_i);
        

    }
}
