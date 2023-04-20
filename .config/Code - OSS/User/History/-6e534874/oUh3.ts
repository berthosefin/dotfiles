import { Product } from "@prisma/client";

export async function getProducts() {
  const response = await fetch("/api/products");
  const data = await response.json();
  return data;
}
