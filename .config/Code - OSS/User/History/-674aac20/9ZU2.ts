import type { NextApiRequest, NextApiResponse } from "next";
import clientPromise from "@/lib/mongodb";
import { ObjectId } from "mongodb";

export default async function getPost(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const client = await clientPromise;
    const db = client.db("posts");
    const { id } = req.query;

    const post = await db.collection("posts").findOne({
      _id: ObjectId(id),
    });

    res.json(posts);
  } catch (e: any) {
    console.log(e);
    throw new Error(e).message;
  }
}
