"use client";

import { createNote } from "@/lib/helper";
import { Note } from "@prisma/client";
import { useState } from "react";
import { useQueryClient, useMutation } from "react-query";

type Props = {
  formData: Note;
  setFormData: () => {};
};

export default function AddNoteForm({ formData, setFormData }: Props) {
  const queryClient = useQueryClient();
  const addMutation = useMutation(createNote);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (Object.keys(formData).length == 0)
      return console.log("Don't have Form Data");
    let { id, title, content } = formData;

    const model = {
      id,
      title,
      content,
    };

    addMutation.mutate(model);
  };

  if (addMutation.isLoading) return <div>Loading...</div>;
  if (addMutation.isError) return <Bug message="Err" />;
  if (addMutation.isSuccess) return <Success message="Added Successsfull" />;

  return (
    <div>
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
