import { createContext, useContext } from "react";

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
