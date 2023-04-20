import { createContext } from "react";

export type User = {
  id?: string;
  name: string;
};

type TTestContext = {
  users: User[];
  createUser: (user: User) => void;
};

export const TTestContext = createContext<TTestContext>({
  users: [],
  createUser(user) {},
});
