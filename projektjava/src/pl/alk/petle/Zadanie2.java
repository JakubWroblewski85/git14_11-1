package pl.alk.petle;

import java.util.Scanner;

public class Zadanie2 {
    public static void main(String[] args) {
        /* Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbe większą od 0");
        int liczba = 0;
        int x = 1;
        while (liczba <= 0) {
            System.out.println("Podaj liczbe wieksza od 0");
            liczba = scanner.nextInt();
        }
        while (x <= liczba) {
            System.out.println(x);
            x++;
        }*/

        // uzytkownika pytamy o ilosc gwazdek ma sie wyswietlic na ekranie
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ile chcesz gwaizdek");
        int liczba = scanner.nextInt();
        while (liczba > 0) {
            System.out.print("*");
            liczba--;
        }
    }
}
