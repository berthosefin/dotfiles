import { QueryClientProvider } from "react-query";
import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body>
        <QueryClientProvider>{children}</QueryClientProvider>
      </body>
    </html>
  );
}
