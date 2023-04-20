import "./globals.css";
import { AppProvider } from "@/components/AppProvider";
import { GlobalContextProvider } from "@/context/store";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body>
        <AppProvider>
          <GlobalContextProvider>{children}</GlobalContextProvider>
        </AppProvider>
      </body>
    </html>
  );
}
