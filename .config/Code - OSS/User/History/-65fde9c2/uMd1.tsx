"use client";

import React from "react";
import { QueryClientProvider, QueryClient } from "react-query";
import { store } from "@/redux/store";
import { Provider } from "react-redux";

const queryClient = new QueryClient();

type Props = {
  children: React.ReactNode;
};

export default function AppProvider({ children }: Props) {
  return (
    <QueryClientProvider client={queryClient}>
      <Provider store={store}>{children}</Provider>
    </QueryClientProvider>
  );
}
