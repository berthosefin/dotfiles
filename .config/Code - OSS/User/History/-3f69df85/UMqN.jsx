// import Image from "next/image";
// import { BiEdit, BiTrashAlt} from "react-icons/bi"

export default function Table() {
  return (
    <table className="min-w-full table-auto">
      <thead>
        <tr className="bg-gray-800">
          <th className="px-16 py-2">
            <span className="text-gray-200">Name</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-gray-200">Email</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-gray-200">Salary</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-gray-200">Birthday</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-gray-200">Status</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-gray-200">Actions</span>
          </th>
        </tr>
      </thead>
      <tbody className="bg-gray-200">
        <tr className="bg-gray-50 text-center">
          <td className="px-16 py-2 flex flex-row items-center">
            {/* <Image src={"#"} width={250} height={250} /> */}
            <img src="#" alt="" />
            <span className="text-center ml-2 font-semibold">Thos</span>
          </td>
          <td className="px-16 py-2">
            <span>thos@gmail.com</span>
          </td>
          <td className="px-16 py-2">
            <span>$ 250</span>
          </td>
          <td className="px-16 py-2">
            <span>13-05-2022</span>
          </td>
          <td className="px-16 py-2">
            <button className="cursor">
              <span className="bg-green-500 px-5 py-1 rounded">Active</span>
            </button>
          </td>
          <td className="px-16 py-2 flex justify-around gap-5">
            <button className="cursor">
              Edit
              {/*<BiEdit size={25} color={"rgb(34,197,94)"}></BiEdit>*/}
            </button>
            <button className="cursor">
              Del
              {/*<BiTrashAlt size={25} color={"rgb(34,197,94)"}></BiTrashAlt>*/}
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  );
}
