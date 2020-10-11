import java.net.*;

public class test {
    public static String downLoadPage(String address){
        URL temp = new URL(address);

        return temp;
    }
    public static void main(String[] args) {
        try {
            // Get hostname by textual representation of IP address
            InetAddress addr = InetAddress.getByName("www.google.com");

            System.out.println(downLoadPage(addr.getCanonicalHostName()));
            }
        catch (UnknownHostException e) {
        }
    }
  }