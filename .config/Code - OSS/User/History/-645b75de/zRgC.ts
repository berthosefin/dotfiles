import { Schema, models, model } from "mongoose";

const useScheme = new Schema({
  name: String,
  avatar: String,
  email: String,
  salary: Number,
  date: String,
  status: String,
});
