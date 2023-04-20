import Link from "next/link";
import "./global.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body>
        <nav>
          <ul>
            <Link href={"/"}>Home</Link>
            <Link href={"/agenda"}>Agenda</Link>
          </ul>
        </nav>
        {children}
      </body>
    </html>
  );
}
