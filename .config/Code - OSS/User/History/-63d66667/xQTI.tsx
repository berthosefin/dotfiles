import Link from "next/link";

export default function Home() {
  return (
    <div className="h-screen w-full homepage">
      <div className="w-4/5 text-center absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
        <h1 className="text-3xl my-8">Explore Tech</h1>
        <Link
          className="shadow-gray-50 bg-[#4C566A] rounded text-xl py-2 px-4 cursor-pointer hover:bg-blue-500 hover:text-white"
          href={"/techGroup"}
        >
          Group of Tech
        </Link>
      </div>
    </div>
  );
}
