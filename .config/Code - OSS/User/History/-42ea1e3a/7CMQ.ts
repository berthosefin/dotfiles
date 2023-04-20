"use client";

import {
  createContext,
  useContext,
  Dispatch,
  SetStateAction,
  useState,
} from "react";

type DataType = {
  name: string;
};

interface ContextProps {
  userId: string;
  setUserId: Dispatch<SetStateAction<string>>;
  data: DataType;
  setData: Dispatch<SetStateAction<DataType[]>>;
}
