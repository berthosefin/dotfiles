import clientPromise from "@/lib/mongodb";
import { ObjectId } from "mongodb";

export default async function deletePost(req, res) {
  try {
    const client = await clientPromise;
    const db = client.db("posts");
    const { id } = req.query;

    const post = await db.collection("posts").deleteOne({
      _id: ObjectId(id),
    });

    res.json(post);
  } catch (e) {
    console.log(e);
    throw new Error(e).message;
  }
}
