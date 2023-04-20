// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/lib/prisma";
import { Product } from "@prisma/client";

type Data = {
  data: Product[];
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  if (req.method === "GET") {
    try {
      const response = await prisma.product.findMany();
    } catch (error: unknown) {
      const err = error as unknown as Error;
    }
  }
}
