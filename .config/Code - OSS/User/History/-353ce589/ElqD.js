import mongoose from "mongoose";
const connection = {};

async function dbConnection() {
  if (connection.isConnected) {
    return;
  }
}
