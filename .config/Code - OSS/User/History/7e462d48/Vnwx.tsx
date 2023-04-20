"use client";

import AddNoteForm from "@/components/AddNoteForm";
import { createNote } from "@/lib/helper";
import { useState } from "react";
import { useQueryClient, useMutation } from "react-query";

export default function Home() {
  const [form, setForm] = useState<FormData>({
    id: "",
    title: "",
    content: "",
  });
  const queryClient = useQueryClient();
  const addMutation = useMutation(createNote);

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
    <div>
      <h1 className="text-center font-bold text-2xl mt-4">Notes</h1>
      <AddNoteForm />
    </div>
  );
}
