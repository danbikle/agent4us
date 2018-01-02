/* Ref:
https://www.mkyong.com/java/java-sha-hashing-example/
2. Hashing String with SHA-256

It will use SHA-256 hashing algorithm to generate a hash value for a password "123456".
*/

package com.mkyong.test;

import java.security.MessageDigest;

public class Main
{
    public static void main(String[] args) throws Exception
    {
        String password = "123456";

        MessageDigest md = MessageDigest.getInstance("SHA-256");
        
        md.update(password.getBytes());

        byte hash_b[] = md.digest();
        
        // I should convert to String so I can see it:
        String hash_s = javax.xml.bind.DatatypeConverter.printHexBinary(hash_b);
        // s.b. 8D969EEF6ECAD3C29A3A629280E686CF0C3F5D5A86AFF3CA12020C923ADC6C92
        
        System.out.println("Hex format : " + hash_s);
    }
}

