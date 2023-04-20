import "./globals.css";
import { AppProvider } from "@/components/AppProvider";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body>
        <AppProvider>{children}</AppProvider>
      </body>
    </html>
  );
}
