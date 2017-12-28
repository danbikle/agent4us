package us.cryp4;

public class Main {
    public static String my_hashf(String in_s) {
        // This function should combine in_s with 256 bits.
        String pad64_s = "01234567"; // This is 8 utf-8 characters which is 64 bits.
        // 256 / 64 is 4
        String pad256_s = pad64_s + pad64_s + pad64_s + pad64_s;
        String out_s    = in_s + pad256_s;
        /* I should return the first 256 bits of out_s.
        256 bits is 32 bytes; I should return the first 32 bytes: */
        return out_s.substring(0,32);
    }
    public static void main(String[] args) {
        String my_in_s = "Today is Dec 27, 2017 and the weather in California is perfect.";
        String out1_s;
        out1_s = my_hashf(my_in_s);
        System.out.println(out1_s);
    }
}
