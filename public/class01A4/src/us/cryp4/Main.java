// Under construction.
/*
Ref:
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

public class Main {

    public static void main(String[] args) throws Exception
    {
        // write your code here
        byte[] buffer= new byte[8192];
	int count_i;
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
	String fileName = "/tmp/Anaconda3-5.0.1-Linux-x86_64.sh";
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(fileName));
    
    
    }
}
