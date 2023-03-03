export interface ProductPrice {
  supermarket: number,
  measurement: string,
  price: number,
  amount: number,
  audit_time: number;
}
interface ProductPriceArray extends Array<ProductPrice> { }

export interface ProductCustom {
  id_product: number,
  product: string,
  description: string,
  supermarkets: ProductPriceArray;
}
export interface ProductCustomArray extends Array<ProductCustom> { }