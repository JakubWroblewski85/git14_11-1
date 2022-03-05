package pl.alk.instrukcje;

import java.util.Locale;
import java.util.Scanner;

public class Przelacznik {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.US);
        int pozycjaMenu;
        float liczba1;
        float liczba2;
        float wynik;
        System.out.println("Podaj pierwsza liczbe");
        liczba1 = scanner.nextFloat();
        System.out.println("Podaj druga liczbe");
        liczba2 = scanner.nextFloat();
        System.out.println("1-dodawanie");
        System.out.println("2-odejmowanie");
        System.out.println("3-mnozenie");
        System.out.println("4-Modulo");
        System.out.println("5-dzielenie");
        pozycjaMenu = scanner.nextInt();
        switch (pozycjaMenu) {
            case 1:
                wynik = liczba1 + liczba2;
                System.out.println("Wynik dodawania: " + wynik);
                break;
            case 2:
                wynik = liczba1 - liczba2;
                System.out.println("Wynik odejmowania: " + wynik);
                break;
            case 3:
                wynik = liczba1 * liczba2;
                System.out.println("Wynik mnozenia: " + wynik);
                break;
            case 4:
                wynik = liczba1 % liczba2;
                System.out.println("Reszta z dzielenia: " + wynik);
                break;
            case 5:
                wynik = liczba1 / liczba2;
                System.out.println("dzielenia: " + wynik);
                break;
            default:
                System.out.println("Zle wybrales/as");
                break;
        }
    }
}

