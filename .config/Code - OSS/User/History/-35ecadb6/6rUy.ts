// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { Employee } from "@prisma/client";
import type { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/lib/prisma";

type Data = {
  data: Employee[];
};

type Exception = {
  error: { message: string };
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data | Exception>
) {
  const { method } = req;

  switch (method) {
    case "GET":
      try {
        const response = await prisma.employee.findMany();
        res.status(200).json({ data: response });
      } catch (err: unknown) {
        const e = err as unknown as Error;
        res.status(400).json({ error: { message: e.message } });
      }
      return;
  }
}
