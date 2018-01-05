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
        String random_msg_s = random_s + msg_s;
        // I should generate the hash:
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        digest.update(random_msg_s.getBytes());
        // I should convert to byte-array so I can see it:
        byte hash_b[] = digest.digest();
        // I should convert to String so I can see it:
        String my_hash_s = javax.xml.bind.DatatypeConverter.printHexBinary(hash_b);
        // I should compare my_hash_s to secure_hash_s:
        return my_hash_s.equals(secure_hash_s);
    }
    
    public static void main(String[] args) throws Exception
    {
        // I should operate rock_isvalid():
        String random_s      = "4D27D9224144319ADD96435E18A625D6FE3CB808DBB5F8F081DC2710DF6D9E83";
        String msg_s         = "paper";
        String secure_hash_s = "98065F86634C6C9A049C88F311767D8C31185F1224558BE37E16B1455E59811C";
        System.out.println(rock_isvalid(random_s, msg_s, secure_hash_s)); // s.b. valid

        random_s      = "0785015D4F26A8821F0C585E9E17D379FEDD33B4DB838A8851C6FEF7E6AB8C9D";
        msg_s         = "paper";
        secure_hash_s = "61CB6B0760BC736D9BB3C0CDA8C30A7B8FEEF54B5FB86701FBEA12724F974B37";
        System.out.println(rock_isvalid(random_s, msg_s, secure_hash_s)); // s.b. valid

        random_s      = "B366B66D443C73EDEB515DDF071DFC138C82C7B55D3477AE51B61BA6AEDAAE24";
        msg_s         = "scissors";
        secure_hash_s = "E9603417A59B33A216151556128D17AC18CE76745677F52F357283AAB5B7ADA4";
        System.out.println(rock_isvalid(random_s, msg_s, secure_hash_s)); // s.b. valid

        random_s      = "2ED12C592641AAA7E149E7FF5ADF51D721A1B94FD0E8D652EF8079A7EEF4E3FF";
        msg_s         = "scissors";
        secure_hash_s = "DBF4C716A18E848B821CB425A8D1A69A37AD6BF6D7B5E3802CC3FAFA9A7CFD21";
        System.out.println(rock_isvalid(random_s, msg_s, secure_hash_s)); // s.b. valid
        
        random_s      = "2ED12C592641AAA7E149E7FF5ADF51D721A1B94FD0E8D652EF8079A7EEF4E3FF";
        msg_s         = "scissors";
        secure_hash_s = "DBF4C716A18E848B821CB425A8D1A69A37AD6BF6D7B5E3802CC3FAFA9A7CFD22";
        System.out.println(rock_isvalid(random_s, msg_s, secure_hash_s)); // s.n.b. valid
    }    
}
