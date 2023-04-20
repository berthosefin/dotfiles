import React, { useState } from "react";
import { User } from "./TestContext";

type TProps = {
  children: React.ReactNode;
};

export default function TestContextProvider({ children }) {
  const [users, setUser] = useState<User[]>([]);
  const createUser = (user: User) => {
    user.id = users.lenght;
  };
  return <div>TestContextProvider</div>;
}
