import prisma from "@/lib/prisma";
import { Employee } from "@prisma/client";
import { NextApiRequest, NextApiResponse } from "next";

type Exception = {
  error: { message: string };
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Employee | Exception | undefined>
) {
  const id = req.query.id as string;

  if (req.method === "GET" && id) {
    try {
      const response = await prisma.employee.findUnique({ where: { id } });
      if (!response) throw new Error("Nothing found.");
      res.status(200).json(response);
    } catch (error: unknown) {
      const err = error as unknown as Error;
      res
        .status(404)
        .json({ error: { message: e.message || "Failed to get the post." } });
    }
    return;
  }

  if (req.method === "PUT" && id) {
    try {
      const response = await prisma.employee.findUnique({ where: { id } });
      await updateUser(req.body as User, String(id));
      res.status(200).json(undefined);
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
      res.status(200).json(undefined);
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

  res.setHeader("Allow", ["GET", "PUT", "DELETE"]);
  res.status(405).end(`Method ${req.method} is not allowed`);
}
