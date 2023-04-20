import prisma from ".";

export async function getUsers() {
  try {
    const users = await prisma.user.finMany();
    return { users };
  } catch (error) {
    return { error };
  }
}
