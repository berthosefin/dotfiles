import { BiPencil, BiTrash } from "react-icons/bi";

export default function Table() {
  return (
    <div>
      <table className="w-full h-full border-spacing-0 border-collapse table-auto">
        <thead className="">
          <tr className="h-20 text-left">
            <th className="py-0 px-6">Full name</th>
            <th className="py-0 px-6">Email</th>
            <th className="py-0 px-6">Address</th>
            <th className="py-0 px-6">Phone</th>
            <th className="py-0 px-6 text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr className="h-20 border-t border-solid border-[#d8dee9]">
            <td className="py-3 px-6">name</td>
            <td className="py-3 px-6">email</td>
            <td className="py-3 px-6">address</td>
            <td className="py-3 px-6">phone</td>
            <td className="py-3 px-6 h-full grid gap-3 items-center grid-cols-2 justify-center">
              <button>
                <BiPencil />
              </button>
              <button>
                <BiTrash />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
