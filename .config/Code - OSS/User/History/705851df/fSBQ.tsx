import { BiUserPlus } from "react-icons/bi";

export default function Header() {
  return (
    <header className="p-6 relative flex items-center justify-between">
      <h1 className="text-3xl">
        Manage <span>Employees</span>
      </h1>
      <button className="p-1 rounded border-none">
        <BiUserPlus /> <span>Add new</span>
      </button>
    </header>
  );
}
