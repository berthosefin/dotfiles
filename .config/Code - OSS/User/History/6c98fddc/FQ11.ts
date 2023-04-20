import { PrismaClient } from "@prisma/client";

const client = global.prisma || new PrismaClient();
