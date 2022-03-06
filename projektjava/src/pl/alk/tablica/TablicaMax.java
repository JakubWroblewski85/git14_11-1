package pl.alk.tablica;

// max tablicy
public class TablicaMax {
    public static void main(String[] args) {
        int[] tablica = {1,-10,8,-3,11,4,0};
        int max = tablica[0];
        for (int i = 0; i < tablica.length; i++) {
            if (tablica[i] > max) {
                max = tablica[i];
            }
        }
        System.out.println(max);
    }
}
