import { createContext, useContext } from "react";

export type User = {
  id?: number;
  name: string;
};

type TTestContext = {
  users: User[];
  createUser: (user: User) => void;
};

export const TestContext = createContext<TTestContext>({
  users: [],
  createUser(user) {},
});

export const useTestContext = () => useContext(TestContext);
