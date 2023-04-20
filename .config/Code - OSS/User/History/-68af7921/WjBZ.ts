import { PrismaClient } from "@prisma/client";

declare global {
    namespace NodeJS {
        interface Global {}
    }
}
const prisma = global.prisma: CustomNodeJsGlobal|| new PrismaClient();

export default prisma;
