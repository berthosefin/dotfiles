import { PrismaClient } from "@prisma/client";

const client = global.prisma || new PrismaClient();
if (process.env.NODE_ENV === "production") global.prisma = client;

export default client;
