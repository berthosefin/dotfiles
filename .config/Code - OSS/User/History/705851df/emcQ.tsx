import { BiUserPlus } from "react-icons/bi";

export default function Header() {
  return (
    <header className="py-4 px-auto relative flex items-center justify-between">
      <h1 className="text-3xl">
        Manage <span>Employees</span>
      </h1>
      <button className="py-4 px-8 rounded border-none flex items-center justify-center text-lg capitalize bg-[#81a1c1] text-[#d8dee9] shadow-md hover:bg-[#88c0d0]">
        <BiUserPlus /> <span>Add new</span>
      </button>
    </header>
  );
}
