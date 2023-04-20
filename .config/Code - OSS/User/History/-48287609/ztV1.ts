import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
  name: String,
  avatar: String,
  email: String,
  salary: Number,
  date: String,
  status: String,
});

const Users = mongoose.models.User || model("user", userSchema);
export default Users;
