package pl.alk.logic;

import java.util.Scanner;

public class zadanie7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbe");
        int liczba = scanner.nextInt();
        boolean wiekszaod10 = liczba > 10;
        boolean rowna0 = liczba == 0;
        boolean mniejsza50 = liczba < 50;
        boolean wiekszarowna20 = liczba >= 20;
        boolean mniejszarowna30 = liczba <= 30;
        boolean roznaod5 = liczba != 5;
        System.out.println("Podana liczba jest większa od 10 "+wiekszaod10);
        System.out.println("Podana liczba jest równa 0 "+rowna0);
        System.out.println("Podana liczba jest mniejsza 50 "+mniejsza50);
        System.out.println("Podana liczba jest większa bądź równa 20 "+wiekszarowna20);
        System.out.println("Podana liczba jest mniejsza bądź równa 30 "+mniejszarowna30);
        System.out.println("Podana liczba jest różna od 5 "+roznaod5);
    }
}
