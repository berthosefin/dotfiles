import "./globals.css";
import Link from "next/link";
import NavLink from "@/components/NavLink";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body className="bg-gray-900">
        <NavLink></NavLink>
        <nav className="p-4 border-b-[1px] border-b-gray-600">
          <ul className="text-slate-100 space-x-4">
            <Link href={"/"}>Home</Link>
            <Link href={"/agenda"}>Agenda</Link>
          </ul>
        </nav>
        {children}
      </body>
    </html>
  );
}
