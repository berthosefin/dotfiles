import clientPromise from "@/lib/mongodb";

export default async function getPosts(req, res) {
  try {
    const client = await clientPromise;
    const db = client.db("posts");

    const posts = await db.collection("posts").find({}).limit(20).toArray();

    res.json(posts);
  } catch (e) {
    console.log(e);
    throw new Error(e).message;
  }
}
