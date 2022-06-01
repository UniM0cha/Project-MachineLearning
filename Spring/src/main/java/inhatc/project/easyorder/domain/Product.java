package inhatc.project.easyorder.domain;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;

@Entity
public class Product {
    @Id
    @GeneratedValue
    private Long productId;
    private String productName;

    @OneToMany(mappedBy = "product")
    private List<Sale> sales = new ArrayList<>();

    @OneToMany(mappedBy = "product")
    private List<Stock> stocks = new ArrayList<>();
}
