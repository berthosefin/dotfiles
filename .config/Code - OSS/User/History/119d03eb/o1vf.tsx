import Image from "next/image";
import { Inter } from "next/font/google";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <main className={styles.main}>
      <h1>Hello World</h1>
      <Link href="/about">Go to about Page</Link>
    </main>
  );
}
