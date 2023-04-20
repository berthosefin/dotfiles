import AddUserForm from "./AddUserForm";
import UpdateUserForm from "./UpdateUserForm";
import { useSelector } from "react-redux";

export default function Form() {
  const [formData, setFormData] = useReducer(formReducer, {});
  const formId = useSelector((state: any) => state.app.client.formId);

  return (
    <div className="container mx-auto py-5">
      {formId ? <UpdateUserForm /> : <AddUserForm />}
    </div>
  );
}
