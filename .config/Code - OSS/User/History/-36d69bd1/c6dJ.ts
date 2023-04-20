import { NextApiRequest, NextApiResponse } from "next";
import prisma from "@/prisma/client";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { id } = req.query;

  if (req.method === "DELETE") {
    await prisma.Agenda.delete({ where: { id } });

    res.status(200).json({ message: "ok" });
  }
}
