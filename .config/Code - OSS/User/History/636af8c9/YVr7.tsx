import 
import "./globals.css";
import ReactQueryWrapper from "@/components/ReactQueryWrapper";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body>
        <ReactQueryWrapper>{children}</ReactQueryW>
      </body>
    </html>
  );
}
