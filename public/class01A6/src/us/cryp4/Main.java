/*
Main.java

This Java-app should create and
demonstrate a function which validates that
SHA-256(r|msg) matches a given secure-hash is True or False.

Ref:
http://cryp4.us/cclases/class01A#rock
*/

package us.cryp4;

import java.security.MessageDigest;

public class Main {

    public static Boolean rock_isvalid(String random_s, String msg_s, String secure_hash_s) throws Exception
    {
	// This function should validate that SHA-256(r|msg) matches a given secure-hash.
	return true;
    }
    
    public static void main(String[] args) throws Exception
    {
	// I should operate rock_isvalid():
	String random_s      = "4D27D9224144319ADD96435E18A625D6FE3CB808DBB5F8F081DC2710DF6D9E83";
	String msg_s         = "paper";
	String secure_hash_s = "98065F86634C6C9A049C88F311767D8C31185F1224558BE37E16B1455E59811C";
	System.out.println(rock_isvalid(random_s, msg_s, secure_hash_s));
    }    
}
