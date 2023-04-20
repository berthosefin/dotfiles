import { BiUserPlus } from "react-icons/bi";

export default function Header() {
  return (
    <header className="">
      <h1>
        Manage <span>Employees</span>
      </h1>
      <button>
        <BiUserPlus /> <span>Add new</span>
      </button>
    </header>
  );
}
