import { prisma } from "@/lib/prisma";
import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";

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

          const user = await prisma;
        },
      },
    }),
  ],
});
