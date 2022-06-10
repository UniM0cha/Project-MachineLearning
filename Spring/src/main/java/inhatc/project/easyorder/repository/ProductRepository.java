package inhatc.project.easyorder.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import inhatc.project.easyorder.domain.Product;

@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    public List<Product> findAll();
}
