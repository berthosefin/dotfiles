import AddUserForm from "./AddUserForm";
import UpdateUserForm from "./UpdateUserForm";
import { useSelector } from "react-redux";

export default function Form() {
  const formId = useSelector((state: any) => state.app.client.formId);
  const flag = false;

  return (
    <div className="container mx-auto py-5">
      {formId ? <AddUserForm /> : <UpdateUserForm />}
    </div>
  );
}
