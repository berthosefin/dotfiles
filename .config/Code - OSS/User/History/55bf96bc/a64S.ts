// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import { User } from "@prisma/client";
import { createUser, getUsers } from "@/lib/prisma/users";

type Data = {
  data: User[];
};

type Exception = {
  error: { message: string };
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "POST") {
    try {
      const response = await createUser(req.body as User);
      return res.status(200).json({ data: [response] });
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      return res.status(500).json({ error: { message: e.message } });
    }
  }

  if (req.method === "GET") {
    try {
      const response = await getUsers();
      return res.status(200).json({ response });
    } catch (error: unknown) {
      const err = error as unknown as Error;
      return res.status(500).json({ error: err.message });
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
