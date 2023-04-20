import type { NextApiRequest, NextApiResponse } from "next";
/** Controller */
import Users from "@/model/user";

export async function getUsers(req: NextApiRequest, res: NextApiResponse) {
  try {
    const users = await Users.find({});
    if (!Users) return res.status(404).json({ error: "Data Not Found" });
    res.status(200).json(users);
  } catch (error) {
    res.status(405).json({ error: "Error while Fetching Data" });
  }
}
