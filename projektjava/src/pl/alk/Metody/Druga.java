package pl.alk.Metody;

public class Druga {
    public static void main(String[] args) {
        int[] tablica = {5, 0, 6, 12, 44, 101, 42, 12, 16, 120, -11, -3};
        int wynik = findMin(tablica);
        System.out.println(wynik);
    }

    /**
     * Zwraca wartosc minimalna ze zbirou liczb
     *
     * @param zbior int[] tablica z danymi
     * @return min int
     */
    public static int findMin(int[] zbior) {
        int min = zbior[0]; //Integer.MIN_VALUE;
        for (int i = 1; i < zbior.length; i++) {
            if (zbior[i] < min) {
                min = zbior[i];
            }
        }
        return min;
    }
}