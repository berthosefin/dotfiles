import React, { useState, useEffect, createContext } from "react";

interface IFormContext {
  visible: boolean;
  toggleVisible?: () => void;
}

const defaultState = {
  visible: false,
};

const FormContext = createContext<IFormContext>(defaultState);

export default FormContext;
