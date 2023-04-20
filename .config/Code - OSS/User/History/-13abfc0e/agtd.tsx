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
            <td>email</td>
            <td>address</td>
            <td>phone</td>
            <td>
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
