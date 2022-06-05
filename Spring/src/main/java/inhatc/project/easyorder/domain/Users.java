package inhatc.project.easyorder.domain;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;

@Entity
public class Users {
    @Id
    private String userId;
    private String password;

    @OneToMany(mappedBy = "user")
    private List<Store> stores = new ArrayList<>();
}
