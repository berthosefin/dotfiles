import "./globals.css";
import Navigator from "@/components/Navigator";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <head />
      <body className="text-black bg-white dark:text-white dark:bg-[#1c1c1c] transition-colors duration-300">
        <Navigator>{children}</Navigator>
      </body>
    </html>
  );
}
