import { prisma } from "@/lib/prisma";
import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { Comparer } from "@reduxjs/toolkit";

// export async function GET(request: Request) {
//   return new Response("Hello, Next.js!");
// }
export default NextAuth({
  providers: [
    Credentials({
      id: "credentials",
      name: "Credentials",
      credentials: {
        email: { label: "Email", type: "text" },
        password: { label: "Password", type: "password" },
      },
      authorize: {
        async authorize(credentials) {
          if (!credentials?.email || !credentials?.password) {
            throw new Error("Email and password required");
          }

          const user = await prisma.user.findUnique({
            where: {
              email: credentials.email,
            },
          });

          if (!user || !user.hashedPassword) {
            throw new Error("Email does not exist");
          }

          const isCorrectPassword = await prisma;
        },
      },
    }),
  ],
});
