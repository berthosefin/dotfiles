import prisma from "./client";

export async function getUsers() {
  try {
    const users = await prisma.user.findMany();
    return { users };
  } catch (error) {
    return { error };
  }
}

export async function createUser(user: User) {
  try {
    const userFormDB = await prisma.user.create({ data: user });
    return { user: userFormDB };
  } catch (error) {
    return { error };
  }
}

export async function getUserById(id) {
  try {
    const user = await prisma.user.findUnique({ where: { id } });
    return { user };
  } catch (error) {
    return { error };
  }
}
