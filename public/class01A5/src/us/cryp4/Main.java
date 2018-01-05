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

public class Main {

    public static void main(String[] args) throws Exception
    {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
	// I should loop through 64 places in a hex integer:
	for (int int_i = 0; int_i < 6; int_i++){
	    System.out.println(int_i);
	}
    }
}
