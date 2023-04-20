"use client";

import { Product } from "@prisma/client";
import Image from "next/image";
import { useEffect, useState } from "react";

export default function Home() {
  const [productsInfo, setProductsInfo] = useState<Product[]>([]);
  useEffect(() => {
    fetch("/api/products")
      .then((response) => response.json())
      .then((json) => setProductsInfo(json));
  }, []);

  console.log(productsInfo);

  return (
    <main className="p-5">
      <div>
        <h2 className="text-2xl">OS</h2>
        <div className="py-4">
          <div className="w-64">
            <div className="bg-blue-100 p-5 rounded-xl">
              <Image
                src="/products/archlinux.png"
                width={280}
                height={280}
                alt="os"
              />
            </div>
            <div className="mt-2">
              <h3 className="font-bold text-lg">Archlinux</h3>
            </div>
            <p className="text-sm mt-2 leading-4">
              Lorem ipsum dolor sit amet consectetur, adipisicing elit.
            </p>
            <div className="flex mt-1">
              <div className="text-2xl font-bold grow">$899</div>
              <button className="bg-emerald-400 text-white py-1 px-3 rounded-xl">
                +
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
