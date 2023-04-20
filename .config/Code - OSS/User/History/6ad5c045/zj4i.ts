import { User } from "@prisma/client";
import { NextApiRequest, NextApiResponse } from "next";
import { updateUser, getUserById, deleteUser } from "@/lib/prisma/users";

type Exception = {
  error: { message: string };
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const id = req.query.id as string;

  if (req.method === "PUT" && id) {
    try {
      await updateUser(req.body as User, String(id));
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      return res.status(400).json({
        error: { message: e.message || "Failed to perform update operation." },
      });
    }
  }
}
