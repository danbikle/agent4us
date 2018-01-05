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

    public static Boolean rock_isvalid(String[] in_a) throws Exception
    {
	return true;
    }
    public static void main(String[] args) throws Exception
    {
	String random_s      = "";
	String msg_s         = "";
	String secure_hash_s = "";
	String[] in_a = {random_s, msg_s, secure_hash_s};
	rock_isvalid(in_a);
    }    
}
