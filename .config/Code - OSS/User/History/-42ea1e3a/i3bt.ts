"use client";

import { createContext, useContext, Dispatch, useState } from "react";

type DataType = {
  name: string;
};

interface ContextProps {
  userId: string;
  setUserId: dis;
}
