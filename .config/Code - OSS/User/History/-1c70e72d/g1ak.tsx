import { Nunito } from "next/font/google";

import "./globals.css";

export const metadata = {
  title: "Airbnb",
  description: "Airbnd clone",
};

const font = Nunito;

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
