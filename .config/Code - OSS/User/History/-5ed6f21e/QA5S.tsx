"use client";

import { BiCheck, BiUserPlus, BiX } from "react-icons/bi";
import Table from "@/components/Table";
import Form from "@/components/Form";
import { useSelector, useDispatch } from "react-redux";
import { toggleChangeAction } from "@/redux/reducer";
import { deleteUser } from "@/lib/helper";

export default function Home() {
  const visible = useSelector((state: any) => state.app.client.toggleForm);
  const deleteId = useSelector((state: any) => state.app.client.deleteId);

  const dispatch = useDispatch();

  const handler = () => {
    dispatch(toggleChangeAction());
  };

  const deleteHandler = async () => {
    if (deleteId) {
      await deleteUser(deleteId);
    }
  };

  const cancelHandler = () => {};

  return (
    <main className="py-5">
      <h1 className="text-xl md:text-3xl text-center font-bold py-10">
        Employe Management
      </h1>
      <div className="container mx-auto flex justify-between py-5 border-b">
        <div className="left flex-gap-3">
          <button
            onClick={handler}
            className="flex bg-indigo-500 text-white px-4 py-2 border rounded-md hover:bg-gray-50 hover:border-indigo-500 hover:text-indigo-500"
          >
            Add Employee
            <span className="px-1">
              <BiUserPlus size={23} />
            </span>
          </button>
        </div>
        {DeleteComponent({ deleteHandler, cancelHandler })}
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
      <button>Are you sure?</button>
      <button
        onClick={deleteHandler}
        className="flex bg-red-500 text-white px-4 py-2 border rounded-md hover:bg-rose-500 hover:border-red-500 hover:text-gray-50"
      >
        Yes
        <span className="px-1">
          <BiX color="rgb(255,255,255)" size={25} />
        </span>
      </button>
      <button
        onClick={cancelHandler}
        className="flex bg-green-500 text-white px-4 py-2 border rounded-md hover:bg-green-500 hover:border-green-500 hover:text-gray-50"
      >
        No
        <span className="px-1">
          <BiCheck color="rgb(255,255,255)" size={25} />
        </span>
      </button>
    </div>
  );
}
