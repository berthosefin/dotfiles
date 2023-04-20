import { NextRequest, NextResponse } from "next/server";
import prisma from "@/prisma/client";

export default async function handler(req: NextRequest, res: NextResponse) {
  if (req.method === "POST") {
    const data = req.body;

    await prisma.Agenda.create({
      data,
    });

    res.status(200).json({ message: "ok" });
  }
}
