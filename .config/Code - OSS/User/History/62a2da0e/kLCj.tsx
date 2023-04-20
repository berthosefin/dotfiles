import Table from "./Table";
// import { BiUserPlus } from "react-icons";

export default function Home() {
  return (
    <main className="py-5">
      <h1 className="text-xl md:text-5xl text-center font-bold py-10">
        Employee Management
      </h1>
      <div className="container mx-auto flex justify-between py-5 border-b">
        <div className="left flex gap-3">
          <button className="flex bg-indigo-500 text-white px-4 py-2 border rounded-md hover:bg-gray-50 hover:border-indigo-500 hover:text-gray-800">
            Add Employee i
          </button>
        </div>
      </div>
      {/* table */}
      <div className="container mx-auto">
        <Table></Table>
      </div>
    </main>
  );
}
