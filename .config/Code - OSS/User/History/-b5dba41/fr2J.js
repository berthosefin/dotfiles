import Client from "@/models/Client";
import dbConnection from "@/services/dbConnection";

dbConnection();

export default async function handler(req, res) {
  const { method } = req;

  switch (method) {
    case "GET":
      try {
        const clients = await Client({});
        res.status(200).json({ success: true, data: clients });
      } catch (error) {
        console.log(error);
      }
  }
}
