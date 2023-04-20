"use client";

import Input from "./Input";
import { useRouter } from "next/navigation";

export default function FormAgenda() {
  const router = useRouter();

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const res = await fetch("/api/agenda", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: formData.get("title"),
        date: formData.get("date"),
        time_start: formData.get("time_start"),
        time_end: formData.get("time_end"),
        place: formData.get("place"),
      }),
    });
    const data = await res.json();
    console.log(data);
    router.refresh();
    e.target.reset();
    router.push("/agenda-list");
  };

  return (
    <div className="grid grid-cols-1 place-items-center">
      <form
        onSubmit={handleSubmit}
        className="bg-[#4c566a] space-y-4 p-4 w-[80vw] md:w-[40vw] rounded"
      >
        <div className="flex flex-col gap-4">
          <label className="text-[#d8dee9] ">Title</label>
          <Input type="text" name="title" placeholder="Title" />
        </div>
        <div className="flex flex-col gap-4">
          <label className="text-[#d8dee9] ">Date</label>
          <Input type="date" name="date" />
        </div>
        <div className="flex flex-col-2">
          <div className="flex flex-col gap-4">
            <label className="text-[#d8dee9] ">Start At</label>
            <Input type="time" name="time_start" />
          </div>
          <div className="flex flex-col gap-4">
            <label className="text-[#d8dee9] ">End At</label>
            <Input type="time" name="time_end" />
          </div>
        </div>
        <div className="flex flex-col gap-4">
          <label className="text-[#d8dee9] ">Place</label>
          <Input type="text" name="place" placeholder="Place" />
        </div>
        <div className="text-center pt-6">
          <button
            className="bg-amber-600 rounded-md hover:bg-amber-700 hover:text-slate-200 text-[#d8dee9] px-6 py-2"
            type="submit"
          >
            Add
          </button>
        </div>
      </form>
    </div>
  );
}
