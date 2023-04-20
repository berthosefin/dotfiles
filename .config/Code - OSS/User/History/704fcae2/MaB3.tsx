"use client";

import { QueryClientProvider, QueryClient } from "react-query";

type Props = {
  children: React.ReactNode;
};

const queryClient = new QueryClient();

export default function ReactQueryWrapper({ children }: Props) {
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}
