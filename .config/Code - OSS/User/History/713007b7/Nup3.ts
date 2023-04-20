/** Controller */
import type { NextApiRequest, NextApiResponse } from "next";
import User from "@/models/User";

export async function getUsers(req: NextApiRequest, res: NextApiResponse) {
  try {
    const users = await User.find({});
    if (!users) return res.status(404).json({ error: "Data Not Found" });
    res.status(200).json(users);
  } catch (error) {
    res.status(405).json({ error: "Error while Fetching Data" });
  }
}
