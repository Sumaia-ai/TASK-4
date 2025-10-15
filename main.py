import java.util.Scanner;

public class Main
{
  public static void main(String[] args) {
    Scanner scan=new Scanner(System.in);
        int a =scan.nextInt();
        int d =scan.nextInt();
        int sum = a+d;
        int prod = a*d;
        if (sum  % 2 == 0 && prod %2 !=0 ){
        System.out.println("TRUE ");
        }
        

       
        
          else {
        System.out.println("False");
         }
       
  }
}