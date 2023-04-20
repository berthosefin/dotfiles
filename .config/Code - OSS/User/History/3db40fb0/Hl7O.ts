import { createContext, ReactNode, useContext } from "react";

type toggleFormType = {
  toggleForm: boolean;
};

const toggleFormContextDefaultValues: toggleFormType = {
  toggleForm: false,
};

const ToggleFormContext = createContext<toggleFormType>(
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
