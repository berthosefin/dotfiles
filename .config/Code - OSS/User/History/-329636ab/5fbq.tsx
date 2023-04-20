import { BiUserPlus, BiPlus } from "react-icons/bi";

export default function Home() {
  return (
    <main className="py-5">
      <div className="container mx-auto border-b">
        <div className="">
          <button className="flex bg-teal-700 text-white px-4 py-2 ml-auto border rounded-md hover:bg-gray-50">
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
                className="border w-full px-5 py-3 focus:outline-none rounded-md mb-2"
              />
            </div>
            <div className="input-type">
              <input
                type="text"
                placeholder="e-mail"
                className="border w-full px-5 py-3 focus:outline-none rounded-md mb-2"
              />
            </div>
            <button
              type="submit"
              className="flex justify-center text-md w-2/6 bg-green-500 text-white px-4 py-2 border rounded-md hover:bg-gray-50 hover:border-green-500 hover:text-green-500"
            >
              Add{" "}
              <span className="px-1">
                <BiPlus size={24}></BiPlus>
              </span>
            </button>
          </form>
        </div>
      </div>
    </main>
  );
}
