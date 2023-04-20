import { createContext, useState } from "react";

const ToggleFormContext = createContext();

export function ToggleFormContext({ children }) {
  const [ToggleForm, setToggleForm] = useState("");

  return (
    <ToggleFormContext.Provider value={{ ToggleForm, setToggleForm }}>
      {children}
    </ToggleFormContext.Provider>
  );
}
