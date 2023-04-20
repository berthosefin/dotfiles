import prisma from "./client";

export async function getUsers() {
  try {
    const users = await prisma.user.findMany();
    return { users };
  } catch (error) {
    return { error };
  }
}

export async function createUsers() {
  try {
    const userFormDB = await prisma.user.findMany();
    return { users };
  } catch (error) {
    return { error };
  }
}
