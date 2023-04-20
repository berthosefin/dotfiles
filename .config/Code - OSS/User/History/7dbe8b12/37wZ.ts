import { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/prisma/client";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "GET") {
    try {
      const data = await prisma.agenda.findMany();
      return res.status(200).json(data);
    } catch (error) {
      return res.status(500).json(error);
    }
  }
  if (req.method === "POST") {
    const data = req.body;

    await prisma.agenda.create({
      data,
    });

    res.status(200).json({ message: "ok" });
  }
}
