import { NextApiRequest, NextResponse } from "next";
import prisma from "@/prisma/client";

type Data = {
  name: string;
};

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

/ Next.js API route support: https:/ / nextjs.org / docs / api -
  routes / introduction;
import type { NextApiRequest, NextApiResponse } from "next";

type Data = {
  name: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  res.status(200).json({ name: "John Doe" });
}
