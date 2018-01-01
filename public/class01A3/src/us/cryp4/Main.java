/*
Main.java

This app should solve a puzzle using a "Puzzle Friendly"
Cryptographic Hash function named SHA-256.

The idea is very simple; this script should 'search' for an integer in a range.

The approach will be simple: start at zero and try each integer in the range.

Ref:
http://cryp4.us/cclasses/class01A#puzzle
https://www.mkyong.com/java/java-sha-hashing-example/
 */

package us.cryp4;

import java.security.MessageDigest;

public class Main {

    public static void main(String[] args) throws Exception
    {

        /* I should find the integer, between 0 through 1e+4, which
	 * gives this hash-digest via SHA-256:
	 */
	String puzzle_digest_s = "2AC5B691FA275BE817B9C8CD1A90D23383CA77C1B20FA4058CAF3DE6260425D2";

	/* I should start solving by specifying a range of
	 * integers. If the range is large, the puzzle will be difficult:
         */
	int range_i = (int) 1.0e4;
	int int_i;
        for (int_i = 0; int_i < range_i; int_i++) {
            // I should convert the number to a string and feed that string to SHA-256:
	    String in_s = Integer.toString(int_i);
	    MessageDigest my_hashlib = MessageDigest.getInstance("SHA-256");
		
	    
	}
        System.out.println(int_i);
        System.out.println("done");
	
	/*
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
	*/
    }
}
