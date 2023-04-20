import type { NextApiRequest, NextApiResponse } from "next";
import clientPromise from "@/lib/mongodb";

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
  } catch (e) {
    console.log(e);
    throw new Error(e).message;
  }
}
