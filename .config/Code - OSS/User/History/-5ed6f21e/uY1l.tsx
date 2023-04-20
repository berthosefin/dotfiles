"use client";

import { BiCheck, BiUserPlus, BiX } from "react-icons/bi";
import Table from "@/components/Table";
import Form from "@/components/Form";
import { useSelector, useDispatch } from "react-redux";
import { toggleChangeAction, deleteAction } from "@/redux/reducer";
import { deleteUser, getUsers } from "@/lib/helper";
import { useQueryClient } from "react-query";

export default function Home() {
  const visible = useSelector((state: any) => state.app.client.toggleForm);
  const deleteId = useSelector((state: any) => state.app.client.deleteId);
  const queryClient = useQueryClient();

  const dispatch = useDispatch();

  const handler = () => {
    dispatch(toggleChangeAction());
  };

  const deleteHandler = async () => {
    if (deleteId) {
      await deleteUser(deleteId);
      await queryClient.prefetchQuery("users", getUsers);
      await dispatch(deleteAction(null));
    }
  };

  const cancelHandler = async () => {
    console.log("cancel");
    await dispatch(deleteAction(null));
  };

  return (
    <main className="py-5">
      <h1 className="text-[#4c566a] text-xl md:text-3xl text-center font-bold py-10">
        Employe Management
      </h1>
      <div className="container mx-auto flex justify-between py-5 border-b border-b[#4c566a]">
        <div className="left flex-gap-3">
          <button
            onClick={handler}
            className="flex bg-[#81a1c1] text-[#d8dee9] px-4 py-2 border rounded-md hover:bg-[#d8dee9] hover:border-[#81a1c1] hover:text-[#81a1c1]"
          >
            Add Employee
            <span className="px-1">
              <BiUserPlus size={23} />
            </span>
          </button>
        </div>
        {deleteId ? DeleteComponent({ deleteHandler, cancelHandler }) : <></>}
      </div>

      {/* collapsable form */}
      {visible ? <Form /> : <></>}

      {/* table */}
      <div className="container mx-auto">
        <Table />
      </div>
    </main>
  );
}

function DeleteComponent({ deleteHandler, cancelHandler }: any) {
  return (
    <div className="flex gap-5">
      <button className="text-[#4c566a]">Are you sure?</button>
      <button
        onClick={deleteHandler}
        className="flex bg-[#bf616a] text-[#d8dee9] px-4 py-2 border rounded-md hover:bg-[#bf616a] hover:border-[#bf616a] hover:text-[#d8dee9]"
      >
        Yes
        <span className="px-1">
          <BiX color="#d8dee9" size={25} />
        </span>
      </button>
      <button
        onClick={cancelHandler}
        className="flex bg-[#a3be8c] text-white px-4 py-2 border rounded-md hover:bg-[#a3be8c] hover:border-[#a3be8c] hover:text-[#d8dee9]"
      >
        No
        <span className="px-1">
          <BiCheck color="#d8dee9" size={25} />
        </span>
      </button>
    </div>
  );
}
