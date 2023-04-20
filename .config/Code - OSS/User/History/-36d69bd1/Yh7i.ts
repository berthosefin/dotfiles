import { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/prisma/client";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "DELETE") {
    const { id } = req.query;

    await prisma.Agenda.delete({ where: { id: id } });

    res.status(200).json({ message: "ok" });
  }
}
