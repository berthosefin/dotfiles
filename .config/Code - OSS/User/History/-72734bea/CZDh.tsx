"use client";

import { QueryClientProvider, QueryClient } from "react-query";
import { store } from "@/redux/store";
import { Provider } from "react-redux";

const queryClient = new QueryClient();

type TProps = {
  children: React.ReactNode;
};

export function AppProvider({ children }: TProps) {
  return (
    <QueryClientProvider client={queryClient}>
      <Provider store={store}>{children}</Provider>
    </QueryClientProvider>
  );
}
