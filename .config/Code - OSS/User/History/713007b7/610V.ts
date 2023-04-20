import type { NextApiRequest, NextApiResponse } from "next";
/** Controller */
import Users from "@/model/user";

export async function getUsers(req: NextApiRequest, res: NextApiResponse) {
  try {
    const users = await Users.find({});
    res.status(200).json({ user: "GET Req" });
  } catch (error) {
    res.status(405).json({ error: "Error while Fetching Data" });
  }
}
