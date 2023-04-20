"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

type Agenda = {
  id: number;
  title: string;
  date: string;
};

export default function Card({ agendaList }: any) {
  const router = useRouter();

  const delAgenda = async (id: number) => {
    const res = await fetch(`/api/agenda/${id}`, { method: "DELETE" });
    const data = await res.json();
    console.log(data);
    router.refresh();
  };

  return agendaList.map((agenda: Agenda) => (
    <div key={agenda.id} className="bg-[#4c566a] rounded p-4 relative">
      <button
        className="absolute top-2 right-4"
        onClick={() => delAgenda(agenda.id)}
      >
        x
      </button>
      <div className="space-y-2">
        <h1 className="text-2xl">{agenda.title}</h1>
        <p>{agenda.date}</p>
      </div>
      <div className="mt-4 text-right">
        <Link
          href={`/agenda-list/${agenda.id}`}
          className="bg-[#81a1c1] rounded-md hover:bg-[#88c0d0] hover:text-slate-20 px-6 py-2"
        >
          Detail
        </Link>
      </div>
    </div>
  ));
}
