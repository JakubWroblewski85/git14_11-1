package pl.alk.klasy;

public class UserService {
    User[] users = new User[4];

    public UserService(User[] users) {
        this.users = users;
    }
    /**
     * Wyszukiwanie po tablicy użytkowników pasującego pola login
     * @param login szukana fraza
     * @return User || null
     */
    public User getUserByLogin(String login) {
        for (User elementTablicy : users) {
            boolean isValid = elementTablicy.login.equals(login); // elementTablicy.login == login
            if (isValid == true) {
                return elementTablicy;
            }
        }
        return null;
    }

    public User getUserByEmail(String email) {
        for (int i = 0; i <= users.length - 1; i++) {
            boolean isValid = users[i].email.equals(email);
            if (isValid) {
                return users[i];
            }
        }
        return null;
    }


}
