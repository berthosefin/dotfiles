import { BiUserPlus, BiPlus } from "react-icons/bi";

export default function Home() {
  return (
    <main className="py-5">
      <div className="container mx-auto">
        <div className="border-b">
          <button className="flex justify-center ml-auto w-1/6 bg-teal-700 text-white px-4 py-2 border rounded-md hover:bg-teal-600">
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
              className="flex justify-center mx-auto w-3/6 bg-teal-700 text-white px-4 py-2 border rounded-md hover:bg-teal-600"
            >
              Add
              <span className="px-1">
                <BiPlus size={24}></BiPlus>
              </span>
            </button>
          </form>
        </div>

        <table className="min-w-full table-auto">
          <thead>
            <tr className="bg-teal-700">
              <th className="px-16 py-2">
                <span className="text-gray-200">Name</span>
              </th>
              <th className="px-16 py-2">
                <span className="text-gray-200">Email</span>
              </th>
              <th className="px-16 py-2">
                <span className="text-gray-200">Actions</span>
              </th>
            </tr>
          </thead>
          <tbody className="bg-gray-200">
            <tr className="bg-gray-50 text-center">
              <td className="px-16 py-2">
                <span>Email</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  );
}
