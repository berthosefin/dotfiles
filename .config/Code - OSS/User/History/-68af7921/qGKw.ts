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

const prisma = global.prisma || new PrismaClient();

export default prisma;
