import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";
import { ProductCustomArray } from "./productos";

@Injectable({
  providedIn: 'root'
})
export class ProductosService {

  constructor(private http: HttpClient) { }
 
  getProductos(): Observable<ProductCustomArray> {
    return this.http.get('http://127.0.0.1:8010/api/v1/products/') as Observable<ProductCustomArray>;
  }
}
