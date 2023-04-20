import { BiEdit, BiTrashAlt } from "react-icons/bi";
import Image from "next/image";
import { useQuery } from "react-query";
import { useSelector, useDispatch } from "react-redux";
import {
  toggleChangeAction,
  updateAction,
  deleteAction,
} from "@/redux/reducer";
import { getUsers } from "@/lib/helper";

export default function Table() {
  const { isLoading, isError, data, error } = useQuery("users", getUsers);

  if (isLoading) return <div>Loading..</div>;
  if (isError) return <div>Got Error {error}</div>;

  return (
    <table className="min-w-full table-auto">
      <thead>
        <tr className="bg-[#4c566a]">
          <th className="px-16 py-2">
            <span className="text-[#d8dee9]">Name</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-[#d8dee9]">Email</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-[#d8dee9]">Salary</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-[#d8dee9]">Birthday</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-[#d8dee9]">Status</span>
          </th>
          <th className="px-16 py-2">
            <span className="text-[#d8dee9]">Action</span>
          </th>
        </tr>
      </thead>
      <tbody className="bg-[#d8dee9]">
        {data.data.map((obj, i) => (
          <Tr {...obj} key={i} />
        ))}
      </tbody>
    </table>
  );
}

function Tr({ id, name, avatar, email, salary, date, status }) {
  const visible = useSelector((state) => state.app.client.toggleForm);
  const dispatch = useDispatch();

  const onUpdate = () => {
    dispatch(toggleChangeAction(id));
    if (visible) {
      dispatch(updateAction(id));
    }
  };

  const onDelete = () => {
    if (!visible) {
      dispatch(deleteAction(id));
    }
  };

  return (
    <tr className="bg-[#d8dee9] text-[#4c566a] text-center">
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
              status == "Active" ? "bg-[#a3be8c]" : "bg-[#bf616a]"
            } text-[#d8dee9] px-5 py-1 rounded-full`}
          >
            {status || "Unknown"}
          </span>
        </button>
      </td>
      <td className="px-16 py-2 flex justify-around gap-5">
        <button className="cursor" onClick={onUpdate}>
          <BiEdit size={25} color={"#a3be8c"} />
        </button>
        <button className="cursor" onClick={onDelete}>
          <BiTrashAlt size={25} color={"#bf616a"} />
        </button>
      </td>
    </tr>
  );
}
