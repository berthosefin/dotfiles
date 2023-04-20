// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { Employee } from "@prisma/client";
import type { NextApiRequest, NextApiResponse } from "next";

type Data = {
  data: Employee;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  const { method } = req;
}
