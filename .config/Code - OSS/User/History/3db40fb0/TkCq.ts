import { createContext, ReactNode, useContext, useState } from "react";

type toggleFormContextType = {
  toggleForm: boolean;
};

const toggleFormContextDefaultValues: toggleFormContextType = {
  toggleForm: null,
};

const ToggleFormContext = createContext<toggleFormContextType>(
  toggleFormContextDefaultValues
);

export function useToggleForm() {
  return useContext(ToggleFormContext);
}

type Props = {
  children: ReactNode;
};

export function ToggleFormProvider({ children }: Props) {
  const [toggleForm, setToggleForm] = useState<boolean>(false);
  const value = { toggleForm };
  return (
    <ToggleFormContext.Provider value={value}>
      {children}
    </ToggleFormContext.Provider>
  );
}
