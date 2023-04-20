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
  res: NextApiResponse<Data | Exception>
) {
  if (req.method === "POST") {
    try {
      const response = await createUser(req.body as User);
      res.status(201).json({ data: [response] });
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      res.status(400).json({ error: { message: e.message } });
    }
    return;
  }

  if (req.method === "GET") {
    try {
      const response = await getUsers();
      res.status(200).json({ data: response });
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      res.status(400).json({ error: { message: e.message } });
    }
    return;
  }

  res.setHeader("Allow", ["GET", "POST"]);
  res.status(405).end(`Method ${req.method} is not allowed`);
}
