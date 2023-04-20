import prisma from ".";

export async function getUsers() {
  try {
    const response = await prisma.user.findMany();
    return response;
  } catch (error: unknown) {
    const err = error as unknown as Error;
    console.error(err.stack);
    throw err.message;
  }
}

export async function getUserById(UserId: string) {
  try {
    const response = await prisma.user.findUnique({ where: { id: UserId } });
    return response;
  } catch (error: unknown) {
    const err = error as unknown as Error;
    console.error(err.stack);
    throw err.message;
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
