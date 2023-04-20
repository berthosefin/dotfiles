import "./globals.css";
import ReactQueryWrapper from "@/components/ReactQueryWrapper";

type Props = {
  children: React.ReactNode;
};

export default function RootLayout({ children }: Props) {
  return (
    <html lang="en">
      <head />
      <body>
        <ReactQueryWrapper>{children}</ReactQueryWrapper>
      </body>
    </html>
  );
}
