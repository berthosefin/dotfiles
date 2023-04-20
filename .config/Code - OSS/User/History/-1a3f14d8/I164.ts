// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/lib/prisma";
import { Category } from "@prisma/client";

type Data = {
  data: Category[];
};

type Exception = {
  error: {
    message: string;
  };
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data | Exception>
) {
  if (req.method === "GET") {
    try {
      const response = await prisma.category.findMany();
      res.status(200).json({ data: response });
    } catch (error: unknown) {
      const err = error as unknown as Error;
      res.status(400).json({ error: { message: err.message } });
    }
    return;
  }

  res.setHeader("Allow", ["GET"]);
  res.status(405).end(`Method ${req.method} not allowed`);
}
