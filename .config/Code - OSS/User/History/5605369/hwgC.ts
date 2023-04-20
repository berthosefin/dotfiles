import bcrypt from "bcrypt";
import { prisma } from "@/lib/prisma";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const { email, name, password }: any = request.body;

    const existingUser = await prisma.user.findUnique({
      where: {
        email,
      },
    });

    if (existingUser) {
      return NextResponse.json({ error });
    }
  } catch (error) {
    console.log(error);
    return NextResponse.json({ error });
  }
  //   const res = await fetch("https://data.mongodb-api.com/...", {
  //     headers: {
  //       "Content-Type": "application/json",
  //       "API-Key": process.env.DATA_API_KEY,
  //     },
  //   });
  //   const data = await res.json();

  //   return NextResponse.json({ data });
}
