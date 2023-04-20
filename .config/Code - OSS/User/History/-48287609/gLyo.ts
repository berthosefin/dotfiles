import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
  name: String,
  avatar: String,
  email: String,
  salary: Number,
  date: String,
  status: String,
});

const Users = mongoose.models.User || mongoose.model("User", UserSchema);
export default Users;
