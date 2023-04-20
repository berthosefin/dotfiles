import { BiUserPlus } from "react-icons/bi";

export default function Header() {
  return (
    <header className="pl-3 pr-6">
      <h1>
        Manage <span>Employees</span>
      </h1>
      <button>
        <BiUserPlus /> <span>Add new</span>
      </button>
    </header>
  );
}
