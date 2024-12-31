import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static void print(Object object) {
        System.out.print(object);
    }

    static String input() throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String str = input.readLine();
        return str;
    }
    public static void main(String args[]) throws IOException{
        String str = input();
        char[] ch = str.toCharArray();
        for (char c: ch) {
            if (Character.isUpperCase(c)) {
                print(Character.toLowerCase(c));
            } else {
                print(Character.toUpperCase(c));
            }
        }
    }
}