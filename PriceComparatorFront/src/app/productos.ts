export interface ProductPrice {
  supermarket: number,
  measurement: string,
  price: number
  amount: number;
}
interface ProductPriceArray extends Array<ProductPrice> { }

export interface ProductCustom {
  id_product: number,
  product: string,
  description: string,
  last_edit: number
  supermarkets: ProductPriceArray
}
export interface ProductCustomArray extends Array<ProductCustom> { }