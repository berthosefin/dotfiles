import { Inter } from "@next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <main className="py-5">
      <h1 className="text-xl md:text-5xl text-center font-bold py-10">
        Employee Management
      </h1>
      <div className="container mx-auto flex justify-between py-5 border-b">
        <div className="left flex gap-3">
          <button>Add Employee</button>
        </div>
      </div>
    </main>
  );
}
