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
        <nav className="p-4 border-b-[1px] border-b-gray-600">
          <ul className="text-slate-100 text-lg space-x-4">
            <NavLink href="/">Home</NavLink>
            <NavLink href={"/agenda-list"}>Agenda</NavLink>
          </ul>
        </nav>
        {children}
      </body>
    </html>
  );
}
