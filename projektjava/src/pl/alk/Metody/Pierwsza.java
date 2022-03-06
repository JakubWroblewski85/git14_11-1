package pl.alk.Metody;

public class Pierwsza {
    public static void main(String[] args) {
//        printText("text do wyswietlenia (tak wyswietlamy teks) --pochyły teks to metoda jest statyczna");
//        printText("text do wyswietlenia");
//        printText("text");
//        printText("java");
//        printText(" "); // to wyswietli bo to nie jest pusty string
//        printText("");
//        printText("");
//        printText(" ta    ");
//        printText("Poniżej kolejne zadanie");
//        int[] liczby = {5, 0, 6, 12, 44, 101, 42, 12, 16, 120};
//        int[] liczby2 = {5, 0, 69, 12, 120};
//        float srednia = sredniaArytmetyczna(liczby);
//        System.out.println(srednia);
//        System.out.println(sredniaArytmetyczna(liczby2));


        String dane = podajImieiNazwisko("Adam","Nowak");
        System.out.println(dane);
        printText(podajImieiNazwisko("Jan","Nowakowski"));
    }

    public static void printText(String text) {
        // pierwszy if nie zaneguje bo nie jest w pelni spelniony wiec sie wszsytko wyswieli
        // if (text.isEmpty() && text.equals("java")) {
        if (text.isEmpty() || text.equals("java")) {
            return;
        }
        System.out.println(text);
    }

    /**
     * Funkcja do liczenia sredniej arytmetycznej
     *
     * @return liczby tablica z liczbami
     * @return float srednia
     */

    public static float sredniaArytmetyczna(int[] liczby) {
        int suma = 0;
        for (int number : liczby) {
            suma += number; // zwieksz o wartosc number (suma = suma + number)
        }
        float srednia = suma / (float) liczby.length;
        return srednia;
    }

    public static String podajImieiNazwisko(String imie, String nazwisko) {
        return "Hello, i'm " + imie + " " + nazwisko;
    }
}















