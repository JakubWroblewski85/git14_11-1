package pl.alk.klasy;

public class Main {
    public static void main(String[] args) {
        //User user1 = new User("adam","haslo123","email@email.pl",33);
        //System.out.println(user1.login);
        //System.out.println(user1.wiek);
        //user1.login = "wojtek";
        // System.out.println(user1.login);

        User[] users = new User[4];
        users[0] = new User("adam","password123","adam@sdfs.pl",34);
        users[1] = new User("wojtek","haslo123","wojtek@sdfs.pl",36);
        users[2] = new User("ola","ola123","ola@sdfs.pl",22);
        users[3] = new User("ewa","ewa123","ewa@sfgds.pl",35);

        UserService service = new UserService(users);
        String login = "wojtek";
        User foundUser = service.getUserByLogin(login);
        if (foundUser != null) {
            System.out.println("Znaleziony uzytkownik ma lat: " + foundUser.wiek);
        } else {
            System.out.println("Nie znaleziono uzytkownika dla loginu "+login);
        }

        User foundUserByEmail = service.getUserByEmail("ola@sdfs.pl");
    }
}