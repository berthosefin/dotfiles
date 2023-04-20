import prisma from "./client";

export async function getUsers() {
  try {
    const users = await prisma.user.findMany();
    return { users };
  } catch (error) {
    return { error };
  }
}

export async function createUsers(user) {
  try {
    const userFormDB = await prisma.user.create({ data: user });
    return { user: userFormDB };
  } catch (error) {
    return { error };
  }
}

export async function getUserById(id) {
  try {
    const userFormDB = await prisma.user.create({ data: user });
    return { user: userFormDB };
  } catch (error) {
    return { error };
  }
}
