"use client";

import Table from "@/components/Table";
import Form from "@/components/Form";
import { useSelector, useDispatch } from "react-redux";
import { toggleChangeAction, deleteAction } from "@/redux/reducer";
import { useQueryClient } from "react-query";
import { BiUserPlus } from "react-icons/bi";
import DeleteForm from "@/components/DeleteForm";
import { deleteUser, getUsers } from "@/lib/helper";

export default function Home() {
  const visible = useSelector((state: any) => state.app.client.toggleForm);
  const deleteId = useSelector((state: any) => state.app.client.deleteId);
  const queryClient = useQueryClient();

  const dispatch = useDispatch();

  const handler = () => {
    dispatch(toggleChangeAction());
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
            className="flex bg-[#81a1c1] text-[#e5e9f0] px-4 py-2 border rounded-md hover:bg-[#e5e9f0] hover:border-[#81a1c1] hover:text-[#81a1c1]"
          >
            Add Employee
            <span className="px-1">
              <BiUserPlus size={23} />
            </span>
          </button>
        </div>
        {deleteId ? DeleteForm({ deleteHandler, cancelHandler }) : <></>}
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
