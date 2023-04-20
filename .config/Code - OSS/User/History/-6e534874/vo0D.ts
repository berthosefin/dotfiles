import { Product } from "@prisma/client";

export async function getProducts() {
  const response = await fetch("/api/products");
}
