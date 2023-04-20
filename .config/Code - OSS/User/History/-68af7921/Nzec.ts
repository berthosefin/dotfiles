import { PrismaClient } from "@prisma/client";

const prisma = global.prisma || new PrismaClient();

export default prisma;
