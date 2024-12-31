import java.time.Clock;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Main {
    public static void main(String args[]) {
        LocalDateTime today = LocalDateTime.now(Clock.systemUTC());
        DateTimeFormatter dateFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        System.out.println(today.format(dateFormat));
    }
}