import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static void print(Object object) {
        System.out.println(object);
    }

    static String input() throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String str = input.readLine();
        return str;
    }
    public static void main(String args[]) throws IOException{
        String str = input();
        int a;
        int b;

        StringTokenizer st = new StringTokenizer(str, " ");
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        print(a + b);
    }
}