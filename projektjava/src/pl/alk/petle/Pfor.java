package pl.alk.petle;

// przykład użycia petli for w pętli for na tablicy

import java.util.Scanner;

public class Pfor {
    public static void main(String[] args) {
        int[][] positions = new int[3][3];
        Scanner scanner = new Scanner(System.in);
        for(int i=0; i<positions[i].length; i++) {
            for(int j=0; j<positions[i].length; j++) {
                System.out.println("Podaj liczbe dla komorki: ["+i+"]["+i+"]");
                positions[i][j] = scanner.nextInt();
            }
        }
    }
}
