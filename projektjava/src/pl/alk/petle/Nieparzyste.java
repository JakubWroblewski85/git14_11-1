package pl.alk.petle;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Nieparzyste {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> parzyste = new ArrayList<>();
        List<Integer> nieparzyste = new ArrayList<>();
        System.out.println("Podaj liczbe od 0");
        int liczba = scanner.nextInt();
        for (int i = 1; i <= liczba; i++) {
            if (i % 2 == 0) {
                continue;
            }
            System.out.println(i);
        }

    }
}
