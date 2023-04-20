import React, { useState } from "react";

type TProps = {
  children: React.ReactNode;
};

export default function TestContextProvider({ children }) {
  const [user, setUser] = useState<User[]>;
  return <div>TestContextProvider</div>;
}
