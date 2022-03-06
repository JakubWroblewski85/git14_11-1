package pl.alk.klasy2;

public class Main {
    public static void main(String[] args) {
        Engine silnik1 = new Engine("LPG");
        Car car1 = new Car("bialy", silnik1);
        car1.setBrand("Ford");
        Car car2 = new Car("granatowy", new Engine("diesel"));
        car2.setBrand("Opel");
        System.out.println("Samochod "+car1.getBrand()+" ma silnik "+car1.engine.typeEngine);
        System.out.println("Samochod "+car2.getBrand()+" ma silnik "+car2.engine.typeEngine);
    }
}
