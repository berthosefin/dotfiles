import { Poppins } from "@next/font/google";

const inter = Poppins({ subsets: ["latin"] });

export default function Home() {
  return (
    <main className="py-5">
      <h1 className="text-xl md:5xl text-center font-bold py-10">
        Employee Management
      </h1>
    </main>
  );
}
