import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body className="max-w-7xl h-full my-16 mx-auto rounded bg-[#e5e9f0] shadow-md overflow-hidden">
        {children}
      </body>
    </html>
  );
}
