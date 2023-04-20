import { Inter } from "@next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <main>
      <h1 className="text-xl md:5xl">Employee Management</h1>
    </main>
  );
}
