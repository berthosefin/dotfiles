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
      <body className="bg-[#2e3440]">
        <nav className="p-4 border-b-[1px] border-[#4c566a]">
          <ul className="text-[#d8dee9] text-lg space-x-4">
            <NavLink href="/">Home</NavLink>
            <NavLink href={"/agenda-list"}>Agenda</NavLink>
          </ul>
        </nav>
        {children}
      </body>
    </html>
  );
}
