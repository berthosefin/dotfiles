import React, { useState, useEffect, createContext } from "react";

const defaultState = {
  visible: false,
};

const FormContext = createContext(defaultState);

export default FormContext;
