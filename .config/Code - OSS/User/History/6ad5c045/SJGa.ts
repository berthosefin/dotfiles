import { User } from "@prisma/client";
import { NextApiRequest, NextApiResponse } from "next";
import { updateUser, getUserById, deleteUser } from "@/lib/prisma/users";

type Exception = {
  error: { message: string };
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<User | Exception | undefined>
) {
  const id = req.query.id as string;

  if (req.method === "PUT" && id) {
    try {
      await updateUser(req.body as User, String(id));
      res.status(204).json(undefined);
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      res.status(400).json({
        error: { message: e.message || "Failed to perform update operation." },
      });
    }
    return;
  }

  if (req.method === "DELETE" && id) {
    try {
      await deleteUser(String(id));
      res.status(204).json(undefined);
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      res.status(400).json({
        error: {
          message: e.message || "Failed to perform delete operation.",
        },
      });
    }
    return;
  }

  if (req.method === "GET" && id) {
    try {
      const response = await getUserById(String(id));
      if (!response) throw new Error("Nothing found.");
      res.status(200).json(response);
    } catch (err: unknown) {
      const e = err as unknown as Error;
      console.log(e.message);
      res
        .status(400)
        .json({ error: { message: e.message || "Failed to get the post." } });
    }
    return;
  }
}
