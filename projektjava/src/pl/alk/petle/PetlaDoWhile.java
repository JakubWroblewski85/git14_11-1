package pl.alk.petle;

import java.util.Scanner;

public class PetlaDoWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // przypisanie 2 zmiennych z wartoscią =0
        int x, y = 0;
        String koniec = "n"; // [t/n]
        do {
            System.out.print("Podaj pierwszą liczbe: ");
            x = scanner.nextInt();
            System.out.print("Podaj drugą liczbe: ");
            y = scanner.nextInt();
            System.out.println("Suma twoich liczb to "+(x+y));
            System.out.print("Czy chcesz kontynuować ? [t/n] ");
            koniec = scanner.next();

        // wykonuj pętle dopuki użytkownik nie wpisze t
        } while (koniec.equals("t"));
    }
}
