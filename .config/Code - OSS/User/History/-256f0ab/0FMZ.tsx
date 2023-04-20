import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body className="max-w-7xl h-full mx- rounded bg-[#d8dee9] shadow-sm">
        {children}
      </body>
    </html>
  );
}
