import AddUserForm from "./AddUserForm";
import UpdateUserForm from "./UpdateUserForm";

export default function Form() {
  const flag = true;
  return (
    <div className="container mx-auto py-5">
      {flag ? <AddUserForm /> : <UpdateUserForm />}
    </div>
  );
}
