"use client";

import { useState } from "react";
import { useQueryClient, useMutation } from "react-query";

type FormData = {
  id: string;
  title: string;
  content: string;
};

export default function Home() {
  const [form, setForm] = useState<FormData>({
    id: "",
    title: "",
    content: "",
  });
  const queryClient = useQueryClient();

  return (
    <div>
      <h1 className="text-center font-bold text-2xl mt-4">Notes</h1>
      <form
        onSubmit={(e) => {
          e.preventDefault();
        }}
        className="w-auto min-w-[25%] max-w-min mx-auto space-y-6 flex flex-col items-stretch"
      >
        <input
          type="text"
          placeholder="Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          className="border-2 rounded border-gray-600 p-1"
        />
        <textarea
          placeholder="Content"
          value={form.content}
          onChange={(e) => setForm({ ...form, content: e.target.value })}
          className="border-2 rounded border-gray-600 p-1"
        />
        <button type="submit" className="bg-blue-500 text-white rounded p-1">
          Add +
        </button>
      </form>
    </div>
  );
}
