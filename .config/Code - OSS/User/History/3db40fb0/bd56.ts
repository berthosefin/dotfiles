import { createContext, ReactNode, useContext } from "react";

type toggleFormContextType = {
  toggleForm: boolean;
};

const toggleFormContextDefaultValues: toggleFormContextType = {
  toggleForm: false,
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
  const value = {};
  return (
    <>
      <toggleFormContext.Provider value={value}>
        {childre}
      </toggleFormContext.Provider>
    </>
  );
}
