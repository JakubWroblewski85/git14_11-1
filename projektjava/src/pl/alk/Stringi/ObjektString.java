package pl.alk.Stringi;
import java.util.Scanner;

public class ObjektString {
    public static void main(String[] args) {
        String pogoda1 = "Pada deszcz";
        String pogoda2 = "Swieci slonce";
        String pogoda3 = "Swieci slonce i jest tecza na pieknym, niebieskim niebie";
        System.out.println(pogoda1+ " ma dlugosc: "+pogoda1.length());
        System.out.println(pogoda2+ " ma dlugosc: "+pogoda2.length());
        System.out.println(pogoda3+ " ma dlugosc: "+pogoda3.length());
        System.out.println(pogoda1.length()+pogoda2.length()+pogoda3.length());
        int pogodaSum = pogoda1.length()+pogoda2.length()+pogoda3.length();
//      lub druga opcja pokazania sumy tych zmiennych >>poniżej
        int pogodaSum2 = (pogoda1+pogoda2+pogoda3).length();
        System.out.println(pogodaSum);
        System.out.println(pogodaSum2);

    }
}
