"use client";

import { useReducer } from "react";
// import { BiPlus } from "react-icons/bi";
import Success from "./Success";
import Bug from "./Bug";

const formReducer = (state, event) => {
  return {
    ...state,
    [event.target.name]: event.target.value,
  };
};

export default function Form() {}
