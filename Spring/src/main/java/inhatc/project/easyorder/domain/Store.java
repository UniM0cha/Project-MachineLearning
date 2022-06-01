package inhatc.project.easyorder.domain;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;

@Entity
public class Store {
    @Id
    @GeneratedValue
    private Long storeId;
    private String storeName;

    @OneToMany(mappedBy = "store")
    private List<Stock> stocks = new ArrayList<>();

    @OneToMany(mappedBy = "store")
    private List<Sale> sales = new ArrayList<>();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private Users user;

}
