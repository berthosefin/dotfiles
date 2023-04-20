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
      res.status(404).json({
        error: { message: err.message || "Failed to get the employee." },
      });
    }
    return;
  }

  if (req.method === "PUT" && id) {
    try {
      await prisma.employee.update({
        where: { id },
        data: req.body,
      });
      res.status(200).json(undefined);
    } catch (error: unknown) {
      const err = error as unknown as Error;
      res.status(400).json({
        error: {
          message: err.message || "Failed to perform update operation.",
        },
      });
    }
    return;
  }

  if (req.method === "DELETE" && id) {
    try {
      await prisma.employee.delete({
        where: { id },
      });
      res.status(200).json(undefined);
    } catch (error: unknown) {
      const err = error as unknown as Error;
      res.status(400).json({
        error: {
          message: err.message || "Failed to perform delete operation.",
        },
      });
    }
    return;
  }

  res.setHeader("Allow", ["GET", "PUT", "DELETE"]);
  res.status(405).end(`Method ${req.method} is not allowed`);
}
