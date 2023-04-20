import { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/prisma/client";

// type Data = {
//   name: string;
// };

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "POST") {
    const data = req.body;

    await prisma.Agenda.create({
      data,
    });

    res.status(200).json({ message: "ok" });
  }
}
