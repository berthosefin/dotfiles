import { createContext } from "react";

type toggleFormType = {
  toggleForm: boolean;
};

const toggleFormContextDefaultValues: toggleFormType = {
  toggleForm: false,
};

const ToggleFormContext = createContext<toggleFormType>;
