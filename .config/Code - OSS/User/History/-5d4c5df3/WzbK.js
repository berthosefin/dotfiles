import clientPromise from "@/lib/mongodb";
import { ObjectId } from "mongodb";

export default async function deletePost(req, res) {
  try {
    const client = await clientPromise;
    const db = client.db("posts");
    const { id } = req.query;
    const { title, content } = req.body;

    const post = await db.collection("posts").updateOne(
      {
        _id: ObjectId(id),
      },
      {
        $set: {
          title: title,
          content: content,
        },
      }
    );

    res.json(post);
  } catch (e) {
    console.log(e);
    throw new Error(e).message;
  }
}
