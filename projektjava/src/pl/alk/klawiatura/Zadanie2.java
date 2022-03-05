package pl.alk.klawiatura;

import java.util.Scanner;

public class Zadanie2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String imie;
        String nazwisko;
        int wiek;
        int wzrost;
        float waga;
        System.out.println("Podaj imie");
        imie = scanner.next();
        System.out.println("Podaj nazwisko");
        nazwisko = scanner.next();
        System.out.println("Podaj wiek");
        wiek = scanner.nextInt();
        System.out.println("Podaj wzrost");
        wzrost = scanner.nextInt();
        System.out.println("Podaj wage");
        waga = scanner.nextFloat();
        System.out.println("Twoje dane to "+imie+" "+nazwisko+", masz "+wiek+" lat, masz "+wzrost+" cm wzrostu oraz wage masz"+waga);

    }
}
