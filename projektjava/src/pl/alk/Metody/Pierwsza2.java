package pl.alk.Metody;

public class Pierwsza2 {
    public static void main(String[] args) {
        String dane = podajImieiNazwisko("Adam", "Nowak");
        System.out.println(dane);
        printText(podajImieiNazwisko("Jan", "Kowlaksi"));
    }

    public static void printText(String text) {
        if (text.isEmpty() || text.equals("java")) {
            return;
        }
        System.out.println(text);
    }

    /**
     * Funkcja do liczenia sredniej arytmetycznej
     *
     * @param liczby tablica z liczbami
     * @return float
     */
    public static float sredniaArytmetyczna(int[] liczby) {
        int suma = 0;
        for (int number : liczby) {
            suma += number; //zwieksz o wartosc number (suma = suma + number)
        }
        float srednia = suma / (float) liczby.length;
        return srednia;
    }

    public static String podajImieiNazwisko(String imie, String nazwisko) {
        return "Hello, i'm " + imie + " " + nazwisko;
    }
}

