import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head />
      <body className="text-black bg-white dark:text-white dark:bg-[#1c1c1c] transition-colors duration-300">
        {children}
      </body>
    </html>
  );
}
