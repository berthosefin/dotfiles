// import mongoose from "mongoose";

// const connectMongo = async () => {
//   try {
//     const { connection } = await mongoose.connect(process.env.MONGO_URI!);
//     if (connection.readyState == 1) {
//       console.log("Database Connected");
//     }
//   } catch (errors) {
//     return Promise.reject(errors);
//   }
// };

// export default connectMongo;
import { MongoClient } from "mongodb";

const URI = process.env.MONGO_URI;
const options = {};

if (!URI) throw new Error("Please add your Mongo URI to .env.local");

let client = new MongoClient(URI, options);
let clientPromise;

if (process.env.MONGO_URI !== "production") {
  if (!global._mongoClientPromise) {
    global._mongoClientPromise = client.connect();
  }

  clientPromise = global._mongoClientPromise;
} else {
  clientPromise = client.connect();
}

export default clientPromise;
