package pl.alk.klawiatura;


import java.util.Scanner;

// zadanie 5 obsluga klawiatury
public class Klawiatura {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int firstValue;
        float secondValue;
        String slowo;
        System.out.println("Podaj liczbe calkowita");
        firstValue = scanner.nextInt();
        System.out.println("Podaj liczbe zmiennoprzecinkowa");
        secondValue = scanner.nextFloat();
        System.out.println("Podaj jakies slowo");
        slowo = scanner.next();
        System.out.println(firstValue);
        System.out.println(secondValue);
        System.out.println(slowo);
    }
}
