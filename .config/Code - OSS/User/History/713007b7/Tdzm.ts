import type { NextApiRequest, NextApiResponse } from "next";
/** Controller */

export async function getUsers(req: NextApiRequest, res: NextApiResponse) {
  try {
  } catch (error) {
    res.status(405).json({ error: "Error while Fetching Data" });
  }
}
