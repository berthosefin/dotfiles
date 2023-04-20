import prisma from "./client";

export async function getUsers() {
  try {
    const users = await prisma.users.findMany();
    return { users };
  } catch (error) {
    return { error };
  }
}
