import { createContext, ReactNode, useContext, useState } from "react";

type toggleFormContextType = {
  toggleForm: boolean;
  toggleFormAction: () => void;
};

const toggleFormContextDefaultValues: toggleFormContextType = {
  toggleForm: false,
  toggleFormAction: () => {},
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

  const toggleFormAction = setToggleForm(!toggleForm);

  const value = {
    toggleForm,
    toggleFormAction,
  };

  return (
    <ToggleFormContext.Provider value={value}>
      {children}
    </ToggleFormContext.Provider>
  );
}
