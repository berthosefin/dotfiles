import { prisma } from "@/lib/prisma";
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { title, content } = req.body;

  if (req.method === "POST") {
    try {
      const response = await prisma.note.create({
        data: {
          title,
          content,
        },
      });
      res.status(200).json({ data: response });
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      res.status(400).json({ error: { message: e.message } });
    }
    return;
  }

  try {
    await prisma.note.create({
      data: {
        title,
        content,
      },
    });
    res.status(200).json({ message: "Note created" });
  } catch (error) {
    res.
  }
}
