import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

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
        float score;
        switch (str) {
            case ("A+"):
                score = 4.3f;
                break;
            case ("A0"):
                score = 4.0f;
                break;
            case ("A-"):
                score = 3.7f;
                break;
            case ("B+"):
                score = 3.3f;
                break;
            case ("B0"):
                score = 3.0f;
                break;
            case ("B-"):
                score = 2.7f;
                break;
            case ("C+"):
                score = 2.3f;
                break;
            case ("C0"):
                score = 2.0f;
                break;
            case ("C-"):
                score = 1.7f;
                break;
            case ("D+"):
                score = 1.3f;
                break;
            case ("D0"):
                score = 1.0f;
                break;
            case ("D-"):
                score = 0.7f;
                break;
            default:
                score = 0.0f;
        }
        print(score);
    }
}