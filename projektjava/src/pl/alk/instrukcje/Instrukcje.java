package pl.alk.instrukcje;

import java.util.Scanner;

public class Instrukcje {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbe");
        int liczba = scanner.nextInt();
        if (liczba % 2 == 0) {
            System.out.println("Podana liczba jest parzysta");

        } else {
            System.out.println("Podana liczba jest nieparzysta");
        }
        if (liczba > 0) {
            System.out.println("Liczba jest większa od 0");
        } else if (liczba < 0) {
            System.out.println("Liczba jest mniejsza od 0");
        } else {
            System.out.println("Liczba jest rowna 0");
        }
    }
}
