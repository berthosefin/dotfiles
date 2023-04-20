import clientPromise from "@/lib/mongodb";

export defaults function (req, res) {
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
