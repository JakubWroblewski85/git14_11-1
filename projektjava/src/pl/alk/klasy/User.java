package pl.alk.klasy;

public class User {
    String login;
    String password;
    String email;
    int wiek;

    public User(String login, String password, String email, int age) {
        this.login = login;
        this.password = password;
        this.email = email;
        wiek = age;
    }
}