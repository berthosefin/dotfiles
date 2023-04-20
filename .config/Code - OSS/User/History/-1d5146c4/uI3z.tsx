import React, { useState, FC, createContext } from "react";

interface IFormContext {
  visible: boolean;
  toggleVisible?: () => void;
}

const defaultState = {
  visible: false,
};

const FormContext = createContext<IFormContext>(defaultState);

export const FormProvider: FC = ({ children }) => {
  const [visible, setVisible] = useState(defaultState.visible);

  const toggleVisible = () => {
    setVisible(!visible);
  };

  return (
    <FormContext.Provider value={{ visible, toggleVisible }}>
      {children}
    </FormContext.Provider>
  );
};

export default FormContext;
