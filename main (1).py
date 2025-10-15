import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int c = scan.nextInt();
        int d = scan.nextInt();

        if ((a % 2 == 0 && d % 2 == 0 && c % 2 != 0) || 
            (a % 2 == 0 && d % 2 != 0 && c % 2 == 0) || 
            (a % 2 != 0 && d % 2 == 0 && c % 2 == 0)) {
            System.out.println("TRUE");
        } else {
            System.out.println("False");
        }
    }
}
