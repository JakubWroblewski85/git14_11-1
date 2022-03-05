package pl.alk.tablica;

import java.util.Scanner;

public class Tablica {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] imiona = new String[3];
        System.out.println("Podaj imie");
        imiona[0] = scanner.next();
        System.out.println("Podaj drugie imie");
        imiona[1] = scanner.next();
        System.out.println("Podaj trzecie imie");
        imiona[2] = scanner.next();
        System.out.println(imiona[2]);
        System.out.println(imiona[1]);
        System.out.println(imiona[0]);

    }
}
