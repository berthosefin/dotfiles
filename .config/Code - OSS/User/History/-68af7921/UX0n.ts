import { PrismaClient } from "@prisma/client";

declare global {
    namespace NodeJS {
        interface Global {}
    }
}
// add prisma to the NodeJS global type
interface CustomNodeJsGlobal extends NodeJS.Global {
    prisma: PrismaClient
}

// Prevent multiple instances of Prisma in development
declare const global: CustomNodeJsGlobal

const prisma = global.prisma: CustomNodeJsGlobal|| new PrismaClient();

export default prisma;
