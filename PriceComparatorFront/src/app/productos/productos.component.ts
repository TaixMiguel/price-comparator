import { Component, OnInit } from '@angular/core';
import { ProductosService } from "../productos.service";

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent implements OnInit {

  constructor(private productosService: ProductosService) { }

  ngOnInit(): void {
    this.getTrivia();
  }

  getTrivia() {
    this.productosService.getProductos().subscribe({
        next: (data) => {
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      }
    )
  }
}
