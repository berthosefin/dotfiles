import { BiCheck, BiX } from "react-icons/bi";

function DeleteComponent({ deleteHandler, cancelHandler }: any) {
  return (
    <div className="flex gap-5">
      <button className="text-[#4c566a]">Are you sure?</button>
      <button
        onClick={deleteHandler}
        className="flex bg-[#bf616a] text-[#e5e9f0] px-4 py-2 border rounded-md hover:bg-[#bf616a] hover:border-[#bf616a] hover:text-[#e5e9f0]"
      >
        Yes
        <span className="px-1">
          <BiX color="#e5e9f0" size={25} />
        </span>
      </button>
      <button
        onClick={cancelHandler}
        className="flex bg-[#a3be8c] text-[#e5e9f0] px-4 py-2 border rounded-md hover:bg-[#a3be8c] hover:border-[#a3be8c] hover:text-[#e5e9f0]"
      >
        No
        <span className="px-1">
          <BiCheck color="#e5e9f0" size={25} />
        </span>
      </button>
    </div>
  );
}
