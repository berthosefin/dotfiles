"use client";

import { QueryClientProvider, QueryClient } from "react-query";

const queryClient = new QueryClient();

type Props = {
  children: React.ReactNode;
};

export default function ReactQueryWrapper({ children }: Props) {
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}
