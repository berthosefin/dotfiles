import clientPromise from "@/lib/mongodb";
import type { NextApiRequest, NextApiResponse } from "next";

export default async function addPost(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const client = await clientPromise;
    const db = client.db("posts");
    const { title, content } = req.body;

    const post = await db.collection("posts").insertOne({
      title,
      content,
    });

    res.json(post);
  } catch (e: any) {
    console.log(e);
    throw new Error(e).message;
  }
}
