import mongoose from "mongoose";
import { stringify } from "querystring";

const ClientSchema = new mongoose.Schema({
  name: String,
  email: String,
  createdAt: {
    type: Date,
    default: new Date(),
  },
});
