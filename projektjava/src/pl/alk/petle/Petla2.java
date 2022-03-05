package pl.alk.petle;

public class Petla2 {
    public static void main(String[] args) {
        int [] values = {1, 65, 5, 10, 12, 58, 23, 24, 20, 12};
        int suma = 0;
        for(int i=0; i < values.length; i++) {
            suma = suma + values[i];
//            ten sam zapis krótszy (to poniżej)
//            suma += values[i];
        }
        System.out.println("Wyświetl sume: "+suma);
        System.out.println(values.length);

    }
}
