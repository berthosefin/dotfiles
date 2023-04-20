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

    const posts = await db.collection("posts").find({}).limit(20).toArray();

    res.json(posts);
  } catch (e: any) {
    console.log(e);
    throw new Error(e).message;
  }
}
