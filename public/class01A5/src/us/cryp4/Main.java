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
        MessageDigest digest    = MessageDigest.getInstance("SHA-256");
    }
}
