import { NextRequest, NextResponse } from "next/server";
import prisma from "@/prisma/client";

export default function handler(req: NextRequest, res: NextResponse) {
  if (req.method === "POST") {
    const data = req.body;
  }
}
