import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
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
        BigDecimal a;
        BigDecimal b;

        StringTokenizer st = new StringTokenizer(str, " ");
        a = new BigDecimal(st.nextToken());
        b = new BigDecimal(st.nextToken());

        try {
            print(a.divide(b));
        } catch (Exception e) {
            print(a.divide(b, 32, BigDecimal.ROUND_DOWN));
        }
    }
}