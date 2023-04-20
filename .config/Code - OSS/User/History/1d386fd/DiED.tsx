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
      <body className="bg-[#d8dee9]">
        <ReactQueryWrapper>{children}</ReactQueryWrapper>
      </body>
    </html>
  );
}
