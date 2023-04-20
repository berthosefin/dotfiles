import { PrismaClient } from "@prisma/client";

declare global {
  namespace NodeJS {
    interface global {}
  }
}
// add prisma to the NodeJS global type
interface CustomNodeJsGlobal extends NodeJS.Global {
  prisma: PrismaClient;
}

// Prevent multiple instances of Prisma Client in development
const prisma = global.prisma || new PrismaClient();

if (process.env.NODE_ENV === "development") global.prisma == prisma;

export default prisma;
