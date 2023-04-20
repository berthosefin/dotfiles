import type { NextApiRequest, NextApiResponse } from "next";
/** Controller */

export async function getUsers(req: NextApiRequest, res: NextApiResponse) {
  try {
    res.status(200).json({ user: "GET Req" });
  } catch (error) {
    res.status(405).json({ error: "Error while Fetching Data" });
  }
}
