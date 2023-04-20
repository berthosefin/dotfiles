import { BiEdit, BiTrashAlt } from "react-icons/bi";
import Image from "next/image";
import { useQuery } from "react-query";
import { useSelector } from "react-redux";

const getUsers = async () => {
  const response = await fetch(`/api/users`);
  const data = await response.json();
  return data;
};

export default function Table() {
  const state = useSelector((state) => state.app.client.toggleForm);
  console.log(state);

  const { isLoading, isError, data, error } = useQuery("users", getUsers);

  if (isLoading) return <div>Loading..</div>;
  if (isError) return <div>Got Error {error}</div>;

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
            <span className="text-gray-200">Action</span>
          </th>
        </tr>
      </thead>
      <tbody className="bg-gray-200">
        {data.data.map((obj, i) => (
          <Tr {...obj} key={i} />
        ))}
      </tbody>
    </table>
  );
}

function Tr({ id, name, avatar, email, salary, date, status }) {
  return (
    <tr className="bg-gray-50 text-center">
      <td className="px-16 py-2 flex flex-row items-center">
        <Image
          src={avatar || "#"}
          alt=""
          width={10}
          height={10}
          className="h-8 w-8 rounded-full object-cover"
        />
        <span className="text-center ml-2 font-semibold">
          {name || "Unknown"}
        </span>
      </td>
      <td className="px-16 py-2">
        <span>{email || "Unknown"}</span>
      </td>
      <td className="px-16 py-2">
        <span>{salary || "Unknown"}</span>
      </td>
      <td className="px-16 py-2">
        <span>{date || "Unknown"}</span>
      </td>
      <td className="px-16 py-2">
        <button className="cursor">
          <span
            className={`${
              status == "Active" ? "bg-green-500" : "bg-rose-500"
            } text-white px-5 py-1 rounded-full`}
          >
            {status || "Unknown"}
          </span>
        </button>
      </td>
      <td className="px-16 py-2 flex justify-around gap-5">
        <button className="cursor" onClick={onUpdate}>
          <BiEdit size={25} color={"rgb(34,197,94)"} />
        </button>
        <button className="cursor">
          <BiTrashAlt size={25} color={"rgb(244,63,94)"} />
        </button>
      </td>
    </tr>
  );
}
