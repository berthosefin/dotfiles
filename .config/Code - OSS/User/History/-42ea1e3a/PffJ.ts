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

export default function TestContextProvider({ children }: TProps) {
  const [users, setUser] = useState<User[]>([]);
  const createUser = (user: User) => {
    user.id = users.length;
    setUser([...users, user]);
  };
  return (
    <TestContext.Provider
      value={{
        users,
        createUser,
      }}
    >
      {children}
    </TestContext.Provider>
  );
}
