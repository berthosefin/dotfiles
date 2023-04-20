import React, { useState } from "react";
import { User } from "./TestContext";

type TProps = {
  children: React.ReactNode;
};

export default function TestContextProvider({ children }) {
  const [users, setUser] = useState<User[]>([]);
  const createUser = (user: User) => {
    user.id = users.length;
    setUser([...users, user]);
  };
  return <TestContext.Provider value={{
    users,
    createUser
  }};
}
