
// Program
package pl.alk.listy;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Listy {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> imiona = new ArrayList<>();
        String imie;
        while (true) {
            System.out.println("Podaj imie: ");
            imie = scanner.next();
            if (imie.equals("-")){
                break;
            }
            imiona.add(imie);
        }
        System.out.println("wprowadzono "+imiona.size()+" imona");
        int size = imiona.size()-1;
        System.out.println("Podaj numer od 0 do "+size);
        int index = scanner.nextInt();
        if (index > size) {
            System.out.println("Podałes liczbę z zakresu większego niz nasza lista, pobieramy maksymalą wartość z naszej listy :)");
            index = size;
        }
        System.out.println("Wybrane imie to "+imiona.get(index));

    }
}
