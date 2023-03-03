import { Component, OnInit } from '@angular/core';
import { ProductCustomArray, ProductPrice } from '../productos';
import { ProductosService } from "../productos.service";

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent implements OnInit {

  productsData: ProductCustomArray = [];

  constructor(private productosService: ProductosService) { }

  ngOnInit(): void {
    this.getProductos();
  }

  getProductos() {
    this.productosService.getProductos().subscribe({
        next: (data) => {
          this.productsData = data;
        },
        error: (error) => {
          console.log(error);
        }
      }
    )
  }

  getPrice(productPrice: ProductPrice) {
    if (productPrice.measurement == 'UNIDAD') {
      let priceUnit: number = productPrice.price / productPrice.amount;
      return parseFloat(priceUnit.toFixed(2)) + '€';
    }

    // Por PESO:
    if (productPrice.amount == 1 || productPrice.amount == 1000)
      return productPrice.price + '€/Kg';

    let priceKilo: number = productPrice.price/productPrice.amount;
    return parseFloat(priceKilo.toFixed(2)) + '€/Kg';
  }
}
