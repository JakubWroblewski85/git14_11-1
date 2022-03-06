package pl.alk.petle;

// przykład użycia petli for w #### tablica x wymiarowa####

import java.util.Scanner;

public class Pfor2 {
    public static void main(String[] args) {
        int[][] positions = new int[3][3];
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < positions[i].length; i++) {
            for (int j = 0; j < positions[i].length; j++) {
                System.out.println("Podaj liczbe dla komorki: [" + i + "][" + i + "]");
                positions[i][j] = scanner.nextInt();
            }
        }
        boolean koniec = false;
        for (int i = 0; i < positions.length; i++) {
            if (koniec) {
                System.out.println("Koniec");
                break;
            }
            for (int j = 0; j < positions[i].length; j++) {
                if (positions[i][j] == 0) {
                    koniec = true;
                    break;
                }
                if (positions[i][j] < 0) {
                    continue;
                }

            }
        }
    }
}
