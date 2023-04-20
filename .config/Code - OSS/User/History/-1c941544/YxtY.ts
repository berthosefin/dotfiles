import {PrismaClient}

declare global {
  namespace globalThis {
    var prisma: PrismaClient;
  }
}
