import { PrismaClient } from "@prisma/client";

declare global {
  namespace NodeJS {
    interface global {}
  }
}

const prisma = global.prisma || new PrismaClient();

export default prisma;
