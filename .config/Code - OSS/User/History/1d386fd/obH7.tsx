"use client";

import "./globals.css";
import { QueryClientProvider, QueryClient } from "react-query";
import { store } from "@/redux/store";
import { Provider } from "react-redux";

const queryClient = new QueryClient();

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body>
        <QueryClientProvider client={queryClient}>
          <Provider store={store}>{children}</Provider>
        </QueryClientProvider>
      </body>
    </html>
  );
}
