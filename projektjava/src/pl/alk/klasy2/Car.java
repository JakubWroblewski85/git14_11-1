package pl.alk.klasy2;

public class Car {
    private String brand;
    String color;
    Engine engine;

    public Car(String kolor, Engine engine) {
        color = kolor;
        this.engine = engine;
    }

    public void setBrand(String marka) {
        brand = marka;
    }

    public String getBrand(){
        return brand;
    }
}
