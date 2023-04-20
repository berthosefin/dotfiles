import { BiPlus } from "react-icons/bi";
import Success from "./Success";
import Bug from "./Bug";
import { useQueryClient, useMutation } from "react-query";
import { createUser, getUsers } from "@/lib/helper";

export default function AddUserForm({ formData, setFormData }: any) {
  const queryClient = useQueryClient();
  const addMutation = useMutation(createUser, {
    onSuccess: () => {
      queryClient.prefetchQuery("users", getUsers);
    },
  });

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (Object.keys(formData).length == 0)
      return console.log("Don't have Form Data");
    let { id, firstname, lastname, email, salary, date, status } = formData;

    const model = {
      id,
      name: `${firstname} ${lastname}`,
      avatar: "/avatar/img_avatar.png",
      email,
      salary,
      date,
      status: status ?? "Active",
    };

    addMutation.mutate(model);
  };

  if (addMutation.isLoading) return <div>Loading...</div>;
  if (addMutation.isError) return <Bug message="Err" />;
  if (addMutation.isSuccess) return <Success message="Added Successsfull" />;

  return (
    <form className="grid lg:grid-cols-2 w-4/6 gap-4" onSubmit={handleSubmit}>
      <div className="input-type">
        <input
          type="text"
          onChange={setFormData}
          name="firstname"
          className="bg-[#e5e9f0] border w-full px-5 py-3 focus:outline-none rounded-md"
          placeholder="Firstname"
        />
      </div>
      <div className="input-type">
        <input
          type="text"
          onChange={setFormData}
          name="lastname"
          className="bg-[#e5e9f0] border w-full px-5 py-3 focus:outline-none rounded-md"
          placeholder="Lastname"
        />
      </div>
      <div className="input-type">
        <input
          type="text"
          onChange={setFormData}
          name="email"
          className="bg-[#e5e9f0] border w-full px-5 py-3 focus:outline-none rounded-md"
          placeholder="Email"
        />
      </div>
      <div className="input-type">
        <input
          type="text"
          onChange={setFormData}
          name="salary"
          className="bg-[#e5e9f0] border w-full px-5 py-3 focus:outline-none rounded-md"
          placeholder="Salary"
        />
      </div>
      <div className="input-type">
        <input
          type="date"
          onChange={setFormData}
          name="date"
          className="bg-[#e5e9f0] border px-5 py-3 focus:outline-none rounded-md"
        />
      </div>

      <div className="flex gap-10 items-center">
        <div className="form-check">
          <input
            type="radio"
            onChange={setFormData}
            value="Active"
            id="radioDefault1"
            name="status"
            className="form-check-input appearance-none rounded-full h-4 w-4 border border-[#e5e9f0] bg-[#e5e9f0] checked:bg-[#a3be8c] checked:border-[#a3be8c] focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer"
          />
          <label
            htmlFor="radioDefault1"
            className="inline-block text-[#4c566a]"
          >
            Active
          </label>
        </div>
        <div className="form-check">
          <input
            type="radio"
            onChange={setFormData}
            value="Inactive"
            id="radioDefault2"
            name="status"
            className="form-check-input appearance-none rounded-full h-4 w-4 border border-[#e5e9f0] bg-[#e5e9f0] checked:bg-[#a3be8c] checked:border-[#a3be8c] focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer"
          />
          <label
            htmlFor="radioDefault2"
            className="inline-block text-[#4c566a]"
          >
            Inactive
          </label>
        </div>
      </div>

      <button className="flex justify-center text-md w-2/6 bg-[#a3be8c] text-[#e5e9f0] px-4 py-2 border rounded-md hover:bg-[#e5e9f0] hover:border-[#a3be8c] hover:text-[#a3be8c]">
        Add
        <span className="px-1">
          <BiPlus size={24} />
        </span>
      </button>
    </form>
  );
}
