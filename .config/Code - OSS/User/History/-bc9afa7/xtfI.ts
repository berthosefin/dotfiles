import React, { useState } from "react";
import { User } from "./TestContext";

type TProps = {
  children: React.ReactNode;
};

export default function TestContextProvider({ children }) {
  const [user, setUser] = useState<User[]>([]);
  return <div>TestContextProvider</div>;
}
