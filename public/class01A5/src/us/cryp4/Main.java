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
	Random rand          = new Random();
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
	int hex_size_i       = 64;
	char[] hex_char_a = new char[hex_size_i];
	// I should loop through 64 places in a hex integer:
	int place_i;
	for (place_i = 0; place_i < hex_size_i; place_i++){
	    int random_i = rand.nextInt(16);
	    char hex_c = Integer.toHexString(random_i).toUpperCase().toCharArray()[0];
	    hex_char_a[place_i] = hex_c;
	}
	String random_s = new String(hex_char_a);
	System.out.println(random_s);
    }
}
