import { BiUserPlus } from "react-icons/bi";

export default function Home() {
  return (
    <main className="py-5">
      <div className="container mx-auto border-b">
        <div className="">
          <button className="flex bg-green-500 text-white px-4 py-2 ml-auto border rounded-md hover:bg-gray-50">
            Add Client
            <span className="px-1">
              <BiUserPlus size={24}></BiUserPlus>
            </span>
          </button>
          <form className="py-2">
            <div className="input-type">
              <input
                type="text"
                placeholder="name"
                className="border w-full px-5 py-3 focus:outline-none rounded-md"
              />
            </div>
          </form>
        </div>
      </div>
    </main>
  );
}
