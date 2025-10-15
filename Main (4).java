import java.util.Scanner;

public class Task4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double num1 = input.nextDouble();
        double num2 = input.nextDouble();

        if ( Math.round(num1 * 1000)==Math.round(num2 * 1000) ) {
            System.out.println("They are same");
        } else {
            System.out.println("They are different");
        }
    }
}

