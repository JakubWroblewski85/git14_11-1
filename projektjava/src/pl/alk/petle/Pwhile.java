package pl.alk.petle;

import java.util.Scanner;

public class Pwhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int liczba;
        int status = 1;
        while (status != 0) {
            System.out.println("Podaj cyfre (0 konczy)");
            liczba = scanner.nextInt();
            if (liczba == 0) {
                status = 0;
                break;
            }

        }

    }

}
