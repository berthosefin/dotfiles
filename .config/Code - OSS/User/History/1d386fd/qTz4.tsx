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
        <ReactQueryWrapper>{children}</ReactQueryWrapper>
      </body>
    </html>
  );
}
