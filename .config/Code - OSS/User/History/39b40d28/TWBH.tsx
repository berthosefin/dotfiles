"use client";

import Input from "./Input";

export default function FormAgenda() {
  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const res = await fetch;
  };

  return (
    <div className="grid grid-cols-1 place-items-center">
      <form
        onSubmit={handleSubmit}
        className="bg-gray-800 space-y-4 p-4 w-[80vw] md:w-[40vw]"
      >
        <div className="flex flex-col gap-4">
          <label className="text-slate-100 ">Title</label>
          <Input type="text" name="title" placeholder="Title" />
        </div>
        <div className="flex flex-col gap-4">
          <label className="text-slate-100 ">Title</label>
          <Input type="date" name="date" />
        </div>
        <div className="flex flex-col gap-4">
          <label className="text-slate-100 ">Title</label>
          <Input type="time" name="time_start" />
        </div>
        <div className="flex flex-col gap-4">
          <label className="text-slate-100 ">Title</label>
          <Input type="time" name="time_end" />
        </div>
        <div className="flex flex-col gap-4">
          <label className="text-slate-100 ">Title</label>
          <Input type="text" name="place" placeholder="Place" />
        </div>
        <div className="text-center pt-6">
          <button
            className="bg-amber-600 rounded-md hover:bg-amber-700 hover:text-slate-200 text-slate-100 px-6 py-2"
            type="submit"
          >
            Add
          </button>
        </div>
      </form>
    </div>
  );
}
