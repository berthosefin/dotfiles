import prisma from ".";

export async function getUsers() {
  try {
    const users = await prisma.user.findMany();
    return { users };
  } catch (error) {
    return { error };
  }
}

export async function getUserById(id: string) {
  try {
    const user = await prisma.user.findUnique({ where: { id } });
    return { user };
  } catch (error) {
    return { error };
  }
}

type TypeUser = {
  name: string;
  avatar: string;
  email: string;
  salary: string;
  date: string;
  status: string;
};

export async function createUser(user: TypeUser) {
  try {
    const userFormDB = await prisma.user.create({ data: user });
    return { user: userFormDB };
  } catch (error) {
    return { error };
  }
}

export async function putUser(id: string) {
  try {
    //
  } catch (error) {
    return { error };
  }
}
