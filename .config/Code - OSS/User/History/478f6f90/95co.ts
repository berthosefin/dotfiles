import { User } from "@prisma/client";
import prisma from ".";

export async function createUser(user: User) {
  try {
    const response = await prisma.user.create({ data: user });
    return response;
  } catch (err: unknown) {
    const e = err as unknown as Error;
    console.error(e.stack);
    throw e.message;
  }
}

export async function updateUser(user: User, userId: string) {
  try {
    const response = await prisma.user.update({
      where: { id: userId },
      data: user,
    });
  } catch (err: unknown) {
    const e = err as unknown as Error;
    console.error(e.stack);
    throw e.message;
  }
}

export async function getUsers() {
  try {
    const response = await prisma.user.findMany();
    return response;
  } catch (err: unknown) {
    const e = err as unknown as Error;
    console.error(e.stack);
    throw e.message;
  }
}

export async function getUserById(UserId: string) {
  try {
    const response = await prisma.user.findUnique({ where: { id: UserId } });
    return response;
  } catch (err: unknown) {
    const e = err as unknown as Error;
    console.error(e.stack);
    throw e.message;
  }
}

export async function deleteUser(userId: string) {
  try {
    const response = await prisma.user.delete({ where: { id: userId } });
    return response;
  } catch (err: unknown) {
    const e = err as unknown as Error;
    console.error(e.stack);
    throw e.message;
  }
}
