import Client from "@/models/Client";
import dbConnection from "@/services/dbConnection";

dbConnection();

export default async function handler(req, res) {
  const { method } = req;
}
