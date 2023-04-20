import { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/prisma/client";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "POST") {
    const data = req.body;

    await prisma.agenda.create({
      data,
    });

    res.status(200).json({ message: "ok" });
  }
}
