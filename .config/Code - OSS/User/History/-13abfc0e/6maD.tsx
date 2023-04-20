import { BiPencil, BiTrash } from "react-icons/bi";

export default function Table() {
  return (
    <div>
      <table className="w-full h-full border-spacing-0 border-collapse table-auto">
        <thead className="">
          <tr className="h-20 text-left">
            <th>Full name</th>
            <th>Email</th>
            <th>Address</th>
            <th>Phone</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>name</td>
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
