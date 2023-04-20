"use client";

import React from "react";
import { QueryClientProvider, QueryClient } from "react-query";

type Props = {
  children: React.ReactNode;
};

export default function AppProvider({ children }: Props) {
  return { children };
}
