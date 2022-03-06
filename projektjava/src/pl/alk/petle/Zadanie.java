package pl.alk.petle;
import java.util.List;
import java.util.ArrayList;

// Przykład w tablicy użycia pętli for (zadanie 1 w break i continue)
public class Zadanie {
    public static void main(String[] args) {
        int[] liczby = {12, 67, 58, 49, 44, 21, 23, 22, 44, 59, 40};
        int ilosc = 0;
        List<Integer> parzyste = new ArrayList<>();
//        petla wykona sie tyle razy ile jest elementow w tablicy
        for (int i=0; i<liczby.length; i++) {
//            jesli indeks w tablicy jest z modulo rowno 0 to:
            if (liczby[i] % 2 == 0) {
                ilosc++; // ilosc = ilosc +1
                parzyste.add(liczby[i]);
            }
        }
        System.out.println("W tablicy jest "+ilosc+" liczby parzyste");
        System.out.println(parzyste);
    }
}
