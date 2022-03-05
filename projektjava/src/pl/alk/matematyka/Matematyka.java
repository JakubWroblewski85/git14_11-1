package pl.alk.matematyka;

import java.util.Scanner;

public class Matematyka {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int first;
        int second;
        System.out.println("Podaj pierwsza liczbe");
        first = scanner.nextInt();
        System.out.println("Podaj druga liczbe");
        second = scanner.nextInt();

        int dodawanie = first+second;
        int odejmowanie = first-second;
        int mnozenie = first*second;
        int multiply = first/second;
        int modulo = first % second;

        System.out.println("Wynik dodawania: "+dodawanie);
        System.out.println("Wynik odejmowania: "+odejmowanie);
        System.out.println("Wynik mnozenia: "+mnozenie);
        System.out.println("Wynik dzielenia: "+multiply);
        System.out.println("Wynik modulo: "+modulo);

//      java zachowuje kolejność działań
        int resultValue = 3 + 5 * 4 - 10 * 2;
        System.out.println(resultValue);

    }
}
