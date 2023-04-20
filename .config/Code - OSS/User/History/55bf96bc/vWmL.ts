// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import { getUsers, createUser } from "@/lib/prisma/users";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "GET") {
    try {
      const { users, error } = await getUsers();
      if (error) throw new Error(error);
      return res.status(200).json({ users });
    } catch (error) {
      return res.status(500).json({ error: { message: error.message } });
    }
  }

  if (req.method === "POST") {
    try {
      const data = req.body;
      const { user, error } = await createUser(data);
      if (error) throw new Error(error);
      return res.status(200).json({ user });
    } catch (error) {
      return res.status(500).json({ error: error.message });
    }
  }

  res.setHeader("Allow", ["GET", "POST"]);
  res.status(405).end(`Method ${req.method} is not allowed`);
}
