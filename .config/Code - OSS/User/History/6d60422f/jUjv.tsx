import Link from "next/link";

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
          <ul></ul>
        </nav>
        {children}
      </body>
    </html>
  );
}
