/* Ref:
https://www.mkyong.com/java/java-sha-hashing-example/
2. Hashing String with SHA-256

It will use SHA-256 hashing algorithm to generate a hash value for a password "123456".
*/

package com.mkyong.test;

import java.security.MessageDigest;

public class Main
{
    public static void main(String[] args)throws Exception
    {
        String password = "123456";

        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(password.getBytes());

        byte byteData[] = md.digest();

        //convert the byte to hex format method 1
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < byteData.length; i++) {
            sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16).substring(1));
        }

        System.out.println("Hex format : " + sb.toString());

        //convert the byte to hex format method 2
        StringBuffer hexString = new StringBuffer();
        for (int i=0;i<byteData.length;i++) {
            String hex=Integer.toHexString(0xff & byteData[i]);
            if(hex.length()==1) hexString.append('0');
            hexString.append(hex);
        }
        System.out.println("Hex format : " + hexString.toString());
    }
}

