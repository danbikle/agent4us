/*
Main.java

This Java-app should calculate a SHA-256 "secure-hash" AKA hash-digest of a large file.

Ref:
http://cryp4.us/cclases/class01A#compare2
https://www.google.com/search?q=In+java+how+to+get+sha-256+hash+of+a+large+file
https://stackoverflow.com/questions/32032851/how-to-calculate-hash-value-of-a-file-in-java

    byte[] buffer= new byte[8192];
    int count;
    MessageDigest digest = MessageDigest.getInstance("SHA-256");
    BufferedInputStream bis = new BufferedInputStream(new FileInputStream(fileName));
    while ((count = bis.read(buffer)) > 0) {
        digest.update(buffer, 0, count);
    }
    byte[] hash = digest.digest();
    System.out.println(new BASE64Encoder().encode(hash));
*/

package us.cryp4;

import java.security.MessageDigest;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.util.Base64;

public class Main {

    public static void main(String[] args) throws Exception
    {
        // write your code here
        byte[] buffer= new byte[8192];
        int count_i;
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        
        // curl https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh > /tmp/Anaconda3-5.0.1-Linux-x86_64.sh
        String fileName = "/tmp/Anaconda3-5.0.1-Linux-x86_64.sh";
        
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(fileName));
        while ((count_i = bis.read(buffer)) > 0) {
            digest.update(buffer, 0, count_i);
        }
        byte[] hash_b         = digest.digest();
        byte[] encoded_hash_b = Base64.getEncoder().encode(hash_b);
	// I should convert to String so I can see it:
        System.out.println(new String(encoded_hash_b));
	// That's how Java encodes the hash for readability.
	// I prefer how Python encodes the hash.
    }
}
